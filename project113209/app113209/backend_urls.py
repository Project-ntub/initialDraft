from django.urls import path
from . import backend_views
from django.views.generic import TemplateView

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
    path('get_user/<int:user_id>/', backend_views.get_user, name='get_user'),
    path('role_management/', backend_views.role_management, name='role_management'),
    path('create_role/', backend_views.create_role, name='create_role'),
    path('edit_role/<int:role_id>/', backend_views.edit_role, name='edit_role'),
    path('delete_role/<int:role_id>/', backend_views.delete_role, name='delete_role'),
    path('history/', backend_views.history, name='history'),
    path('logout_success/', backend_views.logout_success, name='logout_success'),
    path('pending_list/', backend_views.pending_list, name='pending_list'),
    path('assign_role/<int:user_id>/', backend_views.assign_role, name='assign_role'), 
]
