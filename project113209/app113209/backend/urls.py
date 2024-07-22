# app113209/backend/urls.py
from django.urls import path, include
from . import views as backend_views

app_name = 'backend'

urlpatterns = [
    path('login/', backend_views.BackendLoginView.as_view(), name='backend-login'),
    path('logout/', backend_views.BackendLogoutView.as_view(), name='backend-logout'),
    path('register/', backend_views.register, name='backend-register'),
    path('send_verification_code/', backend_views.send_verification_code_backend, name='send_verification_code_backend'),
    path('verify_code/', backend_views.validate_verification_code_backend, name='verify_code_backend'),
    path('approve_user/<int:user_id>/', backend_views.approve_user, name='approve_user'),
    path('forgot_password/', backend_views.forgot_password, name='forgot_password'),
    path('registration_success/', backend_views.registration_success, name='registration_success'),
    path('management/', backend_views.management, name='management'),
    path('dashboard/', backend_views.dashboard, name='dashboard'),
    path('user_management/', backend_views.user_management, name='user_management'),
    path('update_user/<int:user_id>/', backend_views.update_user_department_and_position, name='update_user_department_and_position'),
    path('delete_user/<int:user_id>/', backend_views.delete_user, name='delete_user'),
    path('edit_user/<int:user_id>/', backend_views.edit_user, name='edit_user'),
    path('role_management/', backend_views.role_management, name='role_management'),
    path('module_management/', backend_views.module_management, name='module_management'),
    path('toggle_role_status/<int:role_id>/', backend_views.toggle_role_status, name='toggle_role_status'),
    path('create_role/', backend_views.create_role, name='create_role'),
    path('edit_role/<int:role_id>/', backend_views.edit_role, name='edit_role'),
    path('delete_role/<int:role_id>/', backend_views.delete_role, name='delete_role'),
    path('history/', backend_views.history, name='history'),
    path('logout_success/', backend_views.logout_success, name='logout_success'),
    path('pending_list/', backend_views.pending_list, name='pending_list'),
    path('get_roles_by_module/<int:module_id>/', backend_views.get_roles_by_module, name='get_roles_by_module'),
    path('assign_role_and_module/<int:user_id>/', backend_views.assign_role_and_module, name='assign_role_and_module'),
    path('get_modules/', backend_views.get_modules, name='get_modules'),
    path('create_module/', backend_views.create_module, name='create_module'),
    path('delete_module/<int:module_id>/', backend_views.delete_module, name='delete_module'),
    path('add_permission/<int:role_id>/', backend_views.add_permission, name='add_permission'),
    path('edit_module/', backend_views.edit_module, name='edit_module'),
    path('delete_permission/<int:permission_id>/', backend_views.delete_permission, name='delete_permission'),
    # path('api/', include('app113209.api_urls')),  # 包含 API 路由
    # path('api/roles/', backend_views.get_roles, name='get_roles'),
    # path('api/users/', backend_views.get_users, name='get_users'),
    # path('api/pending_users/', backend_views.get_pending_users, name='get_pending_users'), # Ensure this endpoint exists
    # path('api/approve_user/<int:user_id>/', backend_views.approve_user, name='api_approve_user'), # Ensure this endpoint exists
]
