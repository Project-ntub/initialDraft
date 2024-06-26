# frontend_urls.py
from django.urls import path
from . import frontend_views
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', frontend_views.FrontendLoginView.as_view(), name='frontend-login'),
    path('register/', frontend_views.register, name='frontend-register'),
    path('send_verification_code/', frontend_views.send_verification_code, name='send_verification_code'),
    path('verify_code/', frontend_views.validate_verification_code, name='verify_code'),
    path('verification_sent/', TemplateView.as_view(template_name='frontend/verification_sent.html'), name='verification_sent'),
    path('verification_failure/', TemplateView.as_view(template_name='frontend/verification_failure.html'), name='verification_failure'),
    path('registration_success/', frontend_views.registration_success, name='registration_success'),
    path('home/', frontend_views.home, name='frontend-home'),
    path('verify_otp/', frontend_views.verify_otp, name='frontend-verify_otp'),
]
