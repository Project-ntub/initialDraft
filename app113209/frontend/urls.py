# frontend/urls.py
from django.urls import path
from . import views
app_name = 'frontend'

urlpatterns = [
    path('send_verification_code/', views.send_verification_code, name='send_verification_code'),
    path('register/', views.register, name='register'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password/<str:token>/', views.reset_password, name='reset_password'),
]
