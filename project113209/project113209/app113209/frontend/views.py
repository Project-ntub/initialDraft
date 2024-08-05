import logging
import uuid
import json
from datetime import timedelta
from django.contrib.auth import get_user_model, login
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from app113209.models import User, PasswordResetToken
from django.shortcuts import get_object_or_404
# 顯示分店的圖表
from django.views.decorators.csrf import csrf_exempt
from app113209.models import Chart

logger = logging.getLogger(__name__)

User = get_user_model()

@csrf_exempt
def send_verification_code(request):
    if request.method == 'GET':
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

@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username', f"user_{User.objects.count() + 1}")
            email = data.get('email')
            password = data.get('password')
            confirm_password = data.get('confirmPassword')
            phone = data.get('phone')
            verification_code = data.get('verificationCode')

            if password != confirm_password:
                logger.error("Passwords do not match")
                return JsonResponse({'error': '密碼不匹配'}, status=400)

            try:
                user = User.objects.get(email=email)
                if user.verification_code != verification_code:
                    logger.error(f"Verification code for email {email} is incorrect")
                    return JsonResponse({'error': '驗證碼不正確'}, status=400)
                if user.expiry_time < timezone.now():
                    logger.error(f"Verification code for email {email} expired")
                    return JsonResponse({'error': '驗證碼已過期,請重新獲取'}, status=400)
                user.username = username
                user.phone = phone
                user.set_password(password)
                user.is_verified = True
                user.verification_code = None
                user.expiry_time = None
                user.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                logger.info(f"User {username} registered successfully")
                return JsonResponse({'message': '註冊成功！'}, status=201)
            except User.DoesNotExist:
                user = User.objects.create(email=email, username=username, phone=phone)
                user.set_password(password)
                user.verification_code = verification_code
                user.expiry_time = timezone.now() + timedelta(minutes=5)
                user.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                logger.info(f"User {username} registered successfully")
                return JsonResponse({'message': '註冊成功！'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': '無效的數據格式'}, status=400)
    else:
        return JsonResponse({'error': '無效的請求方法'}, status=405)

def registration_success(request):
    return JsonResponse({'message': '註冊成功！'}, status=200)

# project113209/app113209/frontend/views.py

def forgot_password(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        if not email:
            return JsonResponse({'success': False, 'message': '電子郵件是必填項'}, status=400)
        try:
            user = User.objects.get(email=email)
            token = str(uuid.uuid4())
            expiry_time = timezone.now() + timedelta(hours=1)
            PasswordResetToken.objects.create(user=user, token=token, expiry_time=expiry_time)

            reset_link = f'http://localhost:8082/reset_password/{token}/'
            send_mail(
                '重置您的密碼',
                f'請點擊以下鏈接重置您的密碼：{reset_link}',
                settings.EMAIL_HOST_USER,
                [email]
            )
            return JsonResponse({'success': True, 'message': '重置密碼連結已發送到您的電子郵件。'})
        except User.DoesNotExist:
            return JsonResponse({'success': False, 'message': '該電子郵件沒有註冊。'}, status=400)
    return JsonResponse({'success': False, 'message': '僅支持POST請求'}, status=405)
def reset_password(request, token):
    if request.method == 'POST':
        try:
            reset_token = get_object_or_404(PasswordResetToken, token=token)
            if reset_token.expiry_time < timezone.now():
                return JsonResponse({'success': False, 'message': '重置鏈接已過期。'}, status=400)
            data = json.loads(request.body)
            password = data.get('password')
            if not password:
                return JsonResponse({'success': False, 'message': '密碼是必填項。'}, status=400)
            user = reset_token.user
            user.set_password(password)
            user.save()
            reset_token.delete()
            return JsonResponse({'success': True, 'message': '密碼重置成功！'})
        except PasswordResetToken.DoesNotExist:
            return JsonResponse({'success': False, 'message': '無效的重置鏈接。'}, status=400)
    return JsonResponse({'success': False, 'message': '僅支持POST請求'}, status=405)


@csrf_exempt
def get_branch_chart_data(request, branch_id):
    charts = Chart.objects.filter(branch_id=branch_id).values('chart_type', 'chart_name', 'chart_data')
    return JsonResponse(list(charts), safe=False)
