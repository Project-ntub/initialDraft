import logging
from django.contrib.auth.views import LoginView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import User
from .validators import CustomPasswordValidator
from django.utils import timezone
from datetime import timedelta
import uuid
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings

logger = logging.getLogger(__name__)

class FrontendLoginView(LoginView):
    template_name = 'frontend/login.html'

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('frontend-home')  # 成功登录后重定向到前台首页
        else:
            return render(request, self.template_name, {'error': '用戶名或密碼錯誤'})

def send_verification_code(request):
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

def validate_verification_code(request):
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
            return render(request, 'frontend/register.html', {'error': '密碼不匹配'})

        try:
            user = User.objects.get(email=email)
            if user.verification_code != verification_code:
                logger.error(f"Verification code for email {email} is incorrect")
                return render(request, 'frontend/register.html', {'error': '驗證碼不正確'})
            if user.expiry_time < timezone.now():
                logger.error(f"Verification code for email {email} expired")
                return render(request, 'frontend/register.html', {'error': '驗證碼已過期,請重新獲取'})
            user.username = username
            user.phone = phone
            user.set_password(password)
            user.is_verified = True
            user.verification_code = None
            user.expiry_time = None
            user.save()
            login(request, user)
            logger.info(f"User {username} registered successfully")
            return redirect('frontend-login')  # 重定向到登錄頁面
        except User.DoesNotExist:
            user = User.objects.create(email=email, username=username, phone=phone)
            user.set_password(password)
            user.verification_code = verification_code
            user.expiry_time = timezone.now() + timedelta(minutes=5)
            user.save()
            login(request, user)
            logger.info(f"User {username} registered successfully")
            return redirect('frontend-login')  # 重定向到登錄頁面

    return render(request, 'frontend/register.html')

def home(request):
    return render(request, 'frontend/home.html')
