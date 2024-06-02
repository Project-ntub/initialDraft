from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import User
from django.core.mail import send_mail
from django.conf import settings
import uuid

class CustomLoginView(LoginView):
    template_name = 'login.html'

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)  # 使用 username 进行认证
        if user is not None:
            login(request, user)
            return redirect('management')  # 成功登录后重定向到仪表板
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

@login_required
def management(request):
    return render(request, 'management.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def user_management(request):
    return render(request, 'user_management.html')

@login_required
def role_management(request):
    return render(request, 'role_management.html')

@login_required
def history(request):
    return render(request, 'history.html')

def logout_success(request):
    return render(request, 'logout.html')

class CustomLogoutView(LogoutView):
    next_page = 'login'

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
            phone=phone,
            verification_code=verification_code,
            is_verified=False,
            is_approved=False
        )
        user.set_password(password)  # 正确加密密码
        user.save()
        send_verification_email(user)  # 发送验证邮件
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
            return redirect('password_reset_done')
        except User.DoesNotExist:
            return redirect('password_reset_failed')
    return render(request, 'forgot_password.html')

class AllowIframeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["X-Frame-Options"] = "ALLOWALL"
        return response