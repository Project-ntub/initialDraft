# project113209\app113209\backend\views.py
import logging
import uuid
import json
from app113209.models import User, Role, RolePermission, Module
from app113209.forms import  UserForm, RoleForm, RolePermissionForm
from app113209.validators import CustomPasswordValidator
from app113209.serializers import UserSerializer, RoleSerializer, ModuleSerializer, RolePermissionSerializer
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
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

logger = logging.getLogger(__name__)

User = get_user_model()

class BackendLoginView(LoginView):
    template_name = 'backend/login.html'

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            email = data.get('username')
            password = data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user, backend='app113209.backends.EmailBackend')
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'error': '使用者名稱或密碼錯誤'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': '無效的數據格式'}, status=400)

def history(request):
    return render(request, 'backend/history.html')

class BackendLogoutView(LogoutView):
    next_page = 'backend:logout_success'

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
            return redirect('backend:registration_success')
        except User.DoesNotExist:
            user = User.objects.create(email=email, username=username, phone=phone)
            user.set_password(password)
            user.verification_code = verification_code
            user.expiry_time = timezone.now() + timedelta(minutes=5)
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            logger.info(f"User {username} registered successfully")
            return redirect('backend:registration_success')

    return render(request, 'backend/register.html')

def registration_success(request):
    return render(request, 'backend/registration_success.html')

    
def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
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

def pending_list(request):
    return render(request, 'backend/pending_list.html')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_pending_users(request):
    pending_users = User.objects.filter(is_active=False, is_deleted=False)
    data = list(pending_users.values())
    return JsonResponse(data, safe=False)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def approve_user(request, user_id):
    try:
        user = User.objects.get(id=user_id, is_active=False)
        user.is_active = True
        user.save()
        return JsonResponse({'success': True})
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_deleted=False)
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.filter(is_deleted=False)
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        module_name = request.data.get('module_name')
        if module_name:
            Module.objects.create(name=module_name)
            return Response({'success': True})
        return Response({'success': False, 'message': '模組名稱為必填項'})

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.filter(is_deleted=False)
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        logger.debug('創建角色請求數據: %s', request.data)
        try:
            response = super().create(request, *args, **kwargs)
            logger.debug('角色創建成功: %s', response.data)
            return response
        except Exception as e:
            logger.error('創建角色時發生錯誤: %s', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def toggle_status(self, request, pk=None):
        role = self.get_object()
        role.is_active = not role.is_active
        role.save()
        return Response({'success': True})

class RolePermissionViewSet(viewsets.ModelViewSet):
    queryset = RolePermission.objects.filter(is_deleted=False)
    serializer_class = RolePermissionSerializer
    permission_classes = [IsAuthenticated]


def management(request):
    return render(request, 'backend/management.html')

def dashboard(request):
    return render(request, 'backend/dashboard.html')

@login_required
def user_management(request):
    query = request.GET.get('q', '')
    sort_by = request.GET.get('sort_by', '')
    department_filter = request.GET.get('department', '')

    active_users = User.objects.filter(is_active=True, is_deleted=False)

    if query:
        active_users = active_users.filter(
            Q(username__icontains=query) |
            Q(email__icontains(query)) |
            Q(phone__icontains(query)) |
            Q(department_id__icontains(query)) |
            Q(position_id__icontains(query))
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

@api_view(['POST'])
def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.is_deleted = True
        user.save()
        return Response({'success': True}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_users(request):
    users = User.objects.filter(is_active=True, is_deleted=False)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_roles(request):
    roles = Role.objects.filter(is_deleted=False)
    data = list(roles.values())
    return JsonResponse(data, safe=False)

def get_roles_by_module(request, module_id):
    roles = Role.objects.filter(module_id=module_id, is_deleted=False).values('id', 'name')
    return JsonResponse(list(roles), safe=False)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assign_role_and_module(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    module_id = request.data.get('module')
    role_id = request.data.get('role')

    if module_id:
        user.module_id = module_id
    if role_id:
        user.role_id = role_id
    user.save()

    return JsonResponse({'success': True})


def role_management(request):
    roles = Role.objects.filter(is_deleted=False)
    modules = Module.objects.filter(is_deleted=False)
    return render(request, 'backend/role_management.html', {
        'roles': roles,
        'modules': modules,
        'current_page': 'role_management'
    })

def module_management(request):
    modules = Module.objects.filter(is_deleted=False)
    return render(request, 'backend/module_management.html', {
        'modules': modules,
        'current_page': 'module_management'
    })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_role(request):
    role_data = request.data.get('role', {})
    role_permissions_data = request.data.get('role_permissions', [])

    serializer = RoleSerializer(data=role_data)
    if serializer.is_valid():
        role = serializer.save()

        # 處理權限
        for perm_data in role_permissions_data:
            RolePermission.objects.create(
                role=role,
                permission_name=perm_data.get('permission_name'),
                can_add=perm_data.get('can_add'),
                can_query=perm_data.get('can_query'),
                can_view=perm_data.get('can_view'),
                can_edit=perm_data.get('can_edit'),
                can_delete=perm_data.get('can_delete'),
                can_print=perm_data.get('can_print'),
                can_export=perm_data.get('can_export'),
                can_maintain=perm_data.get('can_maintain')
            )

        return Response({'success': True}, status=status.HTTP_201_CREATED)
    else:
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_role(request, role_id):
    try:
        role = get_object_or_404(Role, id=role_id)
        role_data = request.data['role']
        role_permissions_data = request.data.get('role_permissions', [])

        role.name = role_data['name']
        role.is_active = role_data['is_active']
        role.module_id = role_data['module']
        role.save()

        role.rolepermission_set.all().delete()
        for perm_data in role_permissions_data:
            RolePermission.objects.create(
                role=role,
                permission_name=perm_data['permission_name'],
                can_add=perm_data['can_add'],
                can_query=perm_data['can_query'],
                can_view=perm_data['can_view'],
                can_edit=perm_data['can_edit'],
                can_delete=perm_data['can_delete'],
                can_print=perm_data['can_print'],
                can_export=perm_data['can_export'],
                can_maintain=perm_data['can_maintain']
            )

        return JsonResponse({'success': True})
    except Exception as e:
        logger.error(f"Error editing role: {e}")
        return JsonResponse({'success': False, 'message': str(e)}, status=500)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_role(request, role_id):
    try:
        role = get_object_or_404(Role, id=role_id)
        role.is_deleted = True
        role.save()
        return JsonResponse({'success': True})
    except Role.DoesNotExist:
        return JsonResponse({'error': 'Role not found'}, status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_role_status(request, role_id):
    role = get_object_or_404(Role, id=role_id)
    data = request.data
    role.is_active = data['is_active']
    role.save()
    return JsonResponse({'success': True})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_modules(request):
    modules = Module.objects.filter(is_deleted=False)
    serializer = ModuleSerializer(modules, many=True)
    return Response({'modules': serializer.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_module(request):
    module_name = request.data.get('module_name')
    if not module_name:
        return Response({'success': False, 'message': '模組名稱為必填項'})

    if Module.objects.filter(name=module_name).exists():
        return Response({'success': False, 'message': '模組名稱已存在'})

    Module.objects.create(name=module_name)
    return Response({'success': True})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_module(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    module.is_deleted = True
    module.save()
    return JsonResponse({'success': True})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_module(request):
    data = request.data
    try:
        module = Module.objects.get(id=data['module_id'])
        module.name = data['module_name']
        module.save()
        return JsonResponse({'success': True})
    except Module.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Module not found'})

@api_view(['POST'])
def add_permission(request, role_id):
    role = get_object_or_404(Role, id=role_id)
    form = RolePermissionForm(request.POST)
    if form.is_valid():
        permission = form.save(commit=False)
        permission.role = role
        permission.save()
        return redirect('backend:edit_role', role_id=role_id)
    return render(request, 'backend/add_permission.html', {'form': form, 'role': role})

@api_view(['POST'])
def delete_permission(request, permission_id):
    permission = get_object_or_404(RolePermission, id=permission_id)
    permission.is_deleted = True
    permission.save()
    role_id = permission.role.id
    return redirect('backend:edit_role', role_id=role_id)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_roles_by_module(request, module_id):
    roles = Role.objects.filter(module_id=module_id, is_deleted=False).values('id', 'name')
    return JsonResponse(list(roles), safe=False)

