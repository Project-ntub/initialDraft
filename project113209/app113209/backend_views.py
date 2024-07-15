import logging
import uuid
import json
from .models import User, Role, RolePermission, Module
from .forms import UserForm, RoleForm, RolePermissionForm
from .validators import CustomPasswordValidator
from datetime import timedelta
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView, LogoutView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q


logger = logging.getLogger(__name__)

User = get_user_model()

class BackendLoginView(LoginView):
    template_name = 'backend/login.html'

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(settings.BACKEND_LOGIN_REDIRECT_URL)
        else:
            return render(request, self.template_name, {'error': '用戶名或密碼錯誤'})


def history(request):
    return render(request, 'backend/history.html')

class BackendLogoutView(LogoutView):
    next_page = 'backend:logout_success'  # 登出后重定向到 logout_success 页面

def logout_success(request):
    return render(request, 'backend/logout_success.html')

def send_verification_code_backend(request):
    email = request.GET.get('email')
    if not email:
        logger.error("Email is required")
        return JsonResponse({'success': False, 'message': '電子郵件是必填項'}, status=400)

    try:
        verification_code = str(uuid.uuid4())[:6]
        expiry_time = timezone.now() + timedelta(minutes=5)
        user, created = User.objects.get_or_create(email=email, defaults={
            'verification_code': verification_code,
            'expiry_time': expiry_time
        })
        if not created:
            user.verification_code = verification_code
            user.expiry_time = expiry_time
            user.save()
        send_verification_email(email, verification_code)
        logger.info(f"Verification code {verification_code} sent to {email} with expiry time {expiry_time}")
        return JsonResponse({'success': True, 'message': '驗證碼已發送'})
    except Exception as e:
        logger.error(f"Failed to send verification code to {email}: {e}")
        return JsonResponse({'success': False, 'message': '發送驗證碼失敗,請重試'}, status=500)

def send_verification_email(email, verification_code):
    subject = '請驗證您的電子郵件'
    message = f'您的驗證碼是 {verification_code}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    try:
        send_mail(subject, message, email_from, recipient_list)
    except Exception as e:
        logger.error(f"Failed to send verification email to {email}: {e}")
        return JsonResponse({'success': False, 'message': '發送驗證碼失敗,請重試'}, status=500)

def validate_verification_code_backend(request):
    email = request.GET.get('email')
    code = request.GET.get('code')
    if not email or not code:
        logger.error("Email and code are required")
        return JsonResponse({'success': False, 'message': '電子郵件和驗證碼是必填項'}, status=400)

    try:
        user = User.objects.get(email=email, verification_code=code)
        if user.expiry_time < timezone.now():
            logger.warning(f"Verification code for {email} expired at {user.expiry_time}")
            return JsonResponse({'success': False, 'message': '驗證碼已過期'}, status=400)
        logger.info(f"Verification code for {email} is valid")
        return JsonResponse({'success': True})
    except User.DoesNotExist:
        logger.error(f"Invalid verification code for {email}")
        return JsonResponse({'success': False, 'message': '驗證碼無效'}, status=400)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            username = f"user_{User.objects.count() + 1}"
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone = request.POST.get('phone')
        verification_code = request.POST.get('verification_code')

        if password != confirm_password:
            logger.error("Passwords do not match")
            return render(request, 'backend/register.html', {'error': '密碼不匹配'})

        try:
            user = User.objects.get(email=email)
            if user.verification_code != verification_code:
                logger.error(f"Verification code for email {email} is incorrect")
                return render(request, 'backend/register.html', {'error': '驗證碼不正確'})
            if user.expiry_time < timezone.now():
                logger.error(f"Verification code for email {email} expired")
                return render(request, 'backend/register.html', {'error': '驗證碼已過期,請重新獲取'})
            user.username = username
            user.phone = phone
            user.set_password(password)
            user.is_verified = True
            user.verification_code = None
            user.expiry_time = None
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            logger.info(f"User {username} registered successfully")
            return redirect('backend:registration_success')  # 重定向到註冊成功頁面
        except User.DoesNotExist:
            # 如果用戶不存在,則創建一個新用戶
            user = User.objects.create(email=email, username=username, phone=phone)
            user.set_password(password)
            user.verification_code = verification_code
            user.expiry_time = timezone.now() + timedelta(minutes=5)
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            logger.info(f"User {username} registered successfully")
            return redirect('backend:registration_success')  # 重定向到註冊成功頁面

    return render(request, 'backend/register.html')

def registration_success(request):
    return render(request, 'backend/registration_success.html')

def approve_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.is_approved = True
        user.save()
        return redirect('approval_success')
    except User.DoesNotExist:
        return redirect('approval_failure')

def approval_success(request):
    return render(request, 'backend/approval_success.html')

def approval_failure(request):
    return render(request, 'backend/approval_failure.html')

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            # Generate and send password reset link
            return redirect('password_reset_done')
        except User.DoesNotExist:
            return redirect('password_reset_failed')
    return render(request, 'backend/forgot_password.html')

class AllowIframeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["X-Frame-Options"] = "ALLOWALL"
        return response


# 審核用戶列表
def pending_list(request):
    pending_users = User.objects.filter(is_active=False)
    return render(request, 'backend/pending_list.html', {'pending_users': pending_users})

# 審核用戶
def approve_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = True  # 開通用戶
    user.save()
    return redirect('backend:pending_list')


def management(request):
    return render(request, 'backend/management.html')


def dashboard(request):
    return render(request, 'backend/dashboard.html')


# 用戶管理
def user_management(request):
    query = request.GET.get('q', '')
    sort_by = request.GET.get('sort_by', '')
    department_filter = request.GET.get('department', '')

    active_users = User.objects.filter(is_active=True, is_deleted=False)

    if query:
        active_users = active_users.filter(
            Q(username__icontains=query) |
            Q(email__icontains=query) |
            Q(phone__icontains=query) |
            Q(department_id__icontains=query) |
            Q(position_id__icontains=query)
        )
    
    if department_filter and department_filter != 'all':
        active_users = active_users.filter(department_id=department_filter)

    if sort_by:
        if sort_by == 'name':
            active_users = active_users.order_by('username')
        elif sort_by == 'email':
            active_users = active_users.order_by('email')
        elif sort_by == 'department':
            active_users = active_users.order_by('department_id')
        elif sort_by == 'position':
            active_users = active_users.order_by('position_id')
        elif sort_by == 'creation-time':
            active_users = active_users.order_by('date_joined')
        elif sort_by == 'last-login':
            active_users = active_users.order_by('last_login')

    departments = ["銷售部", "人力資源部", "資訊部", "業務部", "財務部"]
    positions = ["總經理", "經理", "店長"]

    return render(request, 'backend/user_management.html', {
        'active_users': active_users,
        'departments': departments,
        'positions': positions,
        'query': query,
        'sort_by': sort_by,
        'department_filter': department_filter,
    })

# 更新用戶信息，包括部門和職位
def update_user_department_and_position(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')
        user.department_id = request.POST.get('department')
        user.position_id = request.POST.get('position')
        user.save()
        return redirect('backend:user_management')
    return redirect('backend:user_management')
# 刪除用戶
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_deleted = True
    user.save()
    return redirect('backend:user_management')

# 編輯用戶
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    departments = ["銷售部", "人力資源部", "資訊部", "財務部", "業務部"]
    positions = ["總經理", "經理", "店長"]
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('backend:user_management')
    else:
        form = UserForm(instance=user)
    return render(request, 'backend/edit_user.html', {'form': form, 'user': user, 'departments': departments, 'positions': positions})

def get_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    data = {
        'username': user.username,
        'email': user.email,
        'phone': user.phone,
        'department_id': user.department_id,
        'position_id': user.position_id 
    }
    return JsonResponse(data)

def assign_role(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        role_id = request.POST.get('role')
        role = get_object_or_404(Role, id=role_id)
        user.roles.clear()
        user.roles.add(role)
        return redirect('backend:user_management')
    else:
        roles = Role.objects.all()
        return render(request, 'backend/assign_role.html', {'user': user, 'roles': roles})


# 角色管理
def role_management(request):
    roles = Role.objects.filter(is_deleted=False)
    modules = Module.objects.filter(is_deleted=False)
    return render(request, 'backend/role_management.html', {
        'roles': roles,
        'modules': modules,
        'current_page': 'role_management'
    })

#模組管理
def module_management(request):
    modules = Module.objects.filter(is_deleted=False)
    return render(request, 'backend/module_management.html', {
        'modules': modules,
        'current_page': 'module_management'
    })

def create_role(request):
    modules = Module.objects.all()  # 確保從數據庫中獲取所有模組
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('backend:role_management')
    else:
        form = RoleForm()
    return render(request, 'backend/role_form.html', {'form': form, 'is_edit': False, 'modules': modules})


def edit_role(request, role_id):
    role = get_object_or_404(Role, id=role_id)
    if role.is_deleted:
        return redirect('backend:role_management')
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            for permission in role.rolepermission_set.filter(is_deleted=False):
                permission.can_add = 'can_add_' + str(permission.id) in request.POST
                permission.can_query = 'can_query_' + str(permission.id) in request.POST
                permission.can_view = 'can_view_' + str(permission.id) in request.POST
                permission.can_edit = 'can_edit_' + str(permission.id) in request.POST
                permission.can_delete = 'can_delete_' + str(permission.id) in request.POST
                permission.can_print = 'can_print_' + str(permission.id) in request.POST
                permission.can_export = 'can_export_' + str(permission.id) in request.POST
                permission.can_maintain = 'can_maintain_' + str(permission.id) in request.POST
                permission.save()
            return redirect('backend:role_management')
    else:
        form = RoleForm(instance=role)
        role_permissions = role.rolepermission_set.filter(is_deleted=False)
    return render(request, 'backend/role_form.html', {
        'form': form,
        'role_permissions': role_permissions,
        'is_edit': True,
        'role': role
    })


# 刪除角色
def delete_role(request, role_id):
    role = get_object_or_404(Role, id=role_id)
    role.is_deleted = True
    role.save()
    return redirect('backend:role_management')

def toggle_role_status(request, role_id):
    role = get_object_or_404(Role, id=role_id)
    if request.method == 'POST':
        data = json.loads(request.body)
        role.is_active = data['is_active']
        role.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def get_modules(request):
    modules = Role.objects.values_list('module', flat=True).distinct()
    return JsonResponse({'modules': list(modules)})

@csrf_protect
def create_module(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        module_name = data.get('module_name')
        if module_name:
            Module.objects.create(name=module_name)  # 確保這裡只創建模組
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'message': '模組名稱為必填項'})
    return JsonResponse({'success': False, 'message': '無效的請求方法'})


def delete_module(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    module.is_deleted = True
    module.save()
    return redirect('backend:module_management')

@csrf_exempt
def edit_module(request):
    if request.method == 'POST':
        data = josn.loads(request.body)
        try:
            module = Module.objects.get(id=data['module_id'])
            module.name = data['module_name']
            module.save()
            return JsonResponse({'success': True})
        except Module.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Module not found'})
        return JsonResponse({'success': False, 'error': 'Invalid request method'})


def add_permission(request, role_id):
    role = get_object_or_404(Role, id=role_id)
    if request.method == 'POST':
        form = RolePermissionForm(request.POST)
        if form.is_valid():
            permission = form.save(commit=False)
            permission.role = role
            permission.save()
            return redirect('backend:edit_role', role_id=role_id)
    else:
        form = RolePermissionForm()
    return render(request, 'backend/add_permission.html', {'form': form, 'role': role})

def delete_permission(request, permission_id):
    permission = get_object_or_404(RolePermission, id=permission_id)
    permission.is_deleted = True
    permission.save()
    role_id = permission.role.id
    return redirect('backend:edit_role', role_id=role_id)
