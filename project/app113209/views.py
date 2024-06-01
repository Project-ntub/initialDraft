from django.shortcuts import render, redirect
# 如果你使用了自定義 User 模型，確保它被正確導入
# from app113209.models import User  
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings
from .models import User
import uuid

class CustomLoginView(LoginView):
    template_name = 'login.html'  # 確保這個模板在你的模板目錄中

    @method_decorator(csrf_protect)  # 確保登入視圖被 CSRF 保護
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class CustomLogoutView(LogoutView):
    next_page = 'login'  # 確保有一個名為 'login' 的 URL 可以重定向到


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone = request.POST.get('phone')

        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already exists'})
        
        verification_code = uuid.uuid4()
        user = User(
            username=username,
            email=email,
            password=password,
            phone=phone,
            verification_code=verification_code,
            is_verified=False,
            is_approved=False
        )
        user.save()
        return redirect('registration_success')
    return render(request, 'register.html')

def verify(request, verification_code):
    try:
        user = User.objects.get(verification_code=verification_code)
        user.is_verified = True
        user.save()
        return redirect('verification_success')
    except User.DoesNotExist:
        return redirect('verification_failure')

def approve_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.is_approved = True
        user.save()
        return redirect('approval_success')
    except User.DoesNotExist:
        return redirect('approval_failure')

def send_verification_email(user):
    subject = 'Your verification code'
    message = f'Please verify your account using the following code: {user.verification_code}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, email_from, recipient_list)


def registration_success(request):
    return render(request, 'registration_success.html')

def verification_success(request):
    return render(request, 'verification_success.html')

def verification_failure(request):
    return render(request, 'verification_failure.html')

def approval_success(request):
    return render(request, 'approval_success.html')

def approval_failure(request):
    return render(request, 'approval_failure.html')

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            # Generate and send password reset link
            # This part needs to be implemented according to your password reset logic
            return redirect('password_reset_done')
        except User.DoesNotExist:
            return redirect('password_reset_failed')
    return render(request, 'forgot_password.html')