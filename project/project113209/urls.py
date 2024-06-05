from django.contrib import admin
from django.urls import path
from app113209 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('verify/<uuid:verification_code>/', views.verify, name='verify'),
    path('approve_user/<int:user_id>/', views.approve_user, name='approve_user'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('registration_success/', views.registration_success, name='registration_success'),
    path('verification_success/', views.verification_success, name='verification_success'),
    path('verification_failure/', views.verification_failure, name='verification_failure'),
    path('approval_success/', views.approval_success, name='approval_success'),
    path('approval_failure/', views.approval_failure, name='approval_failure'),
    path('management/', views.management, name='management'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user_management/', views.user_management, name='user_management'),  
    path('role_management/', views.role_management, name='role_management'),  
    path('history/', views.history, name='history'), 
    path('logout_success/', views.logout_success, name='logout_success'), 
]
