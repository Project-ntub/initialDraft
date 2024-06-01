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
    path('forgot_password/', views.forgot_password, name='forgot_password'),  # 確保這裡有 forgot_password 的路由
    path('registration_success/', views.registration_success, name='registration_success'),
    path('verification_success/', views.verification_success, name='verification_success'),
    path('verification_failure/', views.verification_failure, name='verification_failure'),
    path('approval_success/', views.approval_success, name='approval_success'),
    path('approval_failure/', views.approval_failure, name='approval_failure'),
    path('dashboard/', views.dashboard, name='dashboard')
]
