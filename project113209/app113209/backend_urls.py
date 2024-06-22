from django.urls import path
from . import backend_views

urlpatterns = [
    path('login/', backend_views.BackendLoginView.as_view(), name='backend-login'),
    path('logout/', backend_views.BackendLogoutView.as_view(), name='backend-logout'),
    path('register/', backend_views.register, name='register'),
    path('verify/<uuid:verification_code>/', backend_views.verify, name='verify'),
    path('approve_user/<int:user_id>/', backend_views.approve_user, name='approve_user'),
    path('forgot_password/', backend_views.forgot_password, name='forgot_password'),
    path('registration_success/', backend_views.registration_success, name='registration_success'),
    path('verification_success/', backend_views.verification_success, name='verification_success'),
    path('verification_failure/', backend_views.verification_failure, name='verification_failure'),
    path('approval_success/', backend_views.approval_success, name='approval_success'),
    path('approval_failure/', backend_views.approval_failure, name='approval_failure'),
    path('management/', backend_views.management, name='management'),
    path('dashboard/', backend_views.dashboard, name='dashboard'),
    path('user_management/', backend_views.user_management, name='user_management'),  
    path('role_management/', backend_views.role_management, name='role_management'),  
    path('history/', backend_views.history, name='history'), 
    path('logout_success/', backend_views.logout_success, name='logout_success'), 
    path('pending_list/', backend_views.pending_list, name='pending_list'),
]
