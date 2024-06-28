import logging
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError
from .models import User
from .validators import CustomPasswordValidator
from django.utils import timezone
from datetime import timedelta
import uuid
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from django.contrib.auth import get_user_model

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
    next_page = 'backend/logout_success'  # 登出后重定向到 logout_success 页面

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

def approve_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.is_approved = True
        user.save()
        return redirect('approval_success')
    except User.DoesNotExist:
        return redirect('approval_failure')

def registration_success(request):
    return render(request, 'backend/registration_success.html')

def verification_success(request):
    return render(request, 'backend/verification_success.html')

def verification_failure(request):
    return render(request, 'backend/verification_failure.html')

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


@user_passes_test(lambda u: u.is_staff)
def pending_list(request):
    pending_users = User.objects.filter(is_active=False)  # 確保欄位拼寫正確
    return render(request, 'backend/pending_list.html', {'pending_users': pending_users})


@user_passes_test(lambda u: u.is_staff)
def approve_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = True  # 開通用户
    user.save()
    return redirect('backend:pending_list')

def management(request):
    return render(request, 'backend/management.html')


def dashboard(request):
    return render(request, 'backend/dashboard.html')


@user_passes_test(lambda u: u.is_staff)
def user_management(request):
    active_users = User.objects.filter(is_active=True)
    departments = ["銷售部", "人力資源部", "資訊部", "市場部", "財務部"]  # 部門選項
    positions = ["經理", "主管", "店長"]  # 職位選項
    return render(request, 'backend/user_management.html', {'active_users': active_users, 'departments': departments, 'positions': positions})


@user_passes_test(lambda u: u.is_staff)
def update_user_department_and_position(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)
        user.department_id = request.POST.get('department')
        user.position_id = request.POST.get('position')
        user.save()
        return redirect('backend:user_management')
    return redirect('backend:user_management')
def role_management(request):
    return render(request, 'backend/role_management.html')