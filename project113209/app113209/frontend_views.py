from django.contrib.auth.views import LoginView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import User
from django.core.mail import send_mail
from django.conf import settings
from django.core.exceptions import ValidationError
from .validators import CustomPasswordValidator
import uuid
from django.http import JsonResponse

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
            return render(request, self.template_name, {'error': 'Invalid username or password'})

def send_verification_code(request):
    email = request.GET.get('email')
    if not email:
        return JsonResponse({'success': False, 'message': 'Email is required'})

    verification_code = str(uuid.uuid4())[:6]
    User.objects.filter(email=email).update(verification_code=verification_code)

    send_verification_email(email, verification_code)
    return JsonResponse({'success': True})

def send_verification_email(email, verification_code):
    subject = '請驗證您的電子郵件'
    message = f'您的驗證碼是 {verification_code}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone = request.POST.get('phone')
        verification_code = request.POST.get('verification_code')

        if password != confirm_password:
            return render(request, 'frontend/register.html', {'error': '密碼不匹配'})

        if User.objects.filter(email=email).exists() and not User.objects.filter(email=email, verification_code=verification_code).exists():
            return render(request, 'frontend/register.html', {'error': '電子郵件已存在或驗證碼不正確'})

        if User.objects.filter(phone=phone).exists():
            return render(request, 'frontend/register.html', {'error': '電話號碼已存在'})

        password_validator = CustomPasswordValidator()
        try:
            password_validator.validate(password)
        except ValidationError as e:
            error_message = '; '.join(e.messages)
            return render(request, 'frontend/register.html', {'error': error_message})

        try:
            user = User.objects.get(email=email, verification_code=verification_code)
            user.username = username
            user.phone = phone
            user.set_password(password)
            user.is_verified = True
            user.verification_code = None  # 清除验证码，防止重复使用
            user.save()
            login(request, user)
            return redirect('frontend-home')
        except User.DoesNotExist:
            return render(request, 'frontend/register.html', {'error': 'Invalid verification code or email'})
    return render(request, 'frontend/register.html')

def home(request):
    return render(request, 'frontend/home.html')
