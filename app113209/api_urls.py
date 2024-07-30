from django.urls import path
from app113209.frontend import views as frontend_views

urlpatterns = [
    path('send_verification_code/', frontend_views.send_verification_code, name='send_verification_code'),
    path('register/', frontend_views.register, name='register'),
]
