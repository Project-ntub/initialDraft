from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import UserViewSet, ModuleViewSet, RoleViewSet, RolePermissionViewSet
from .views import (
    get_modules, 
    get_roles_by_module, 
    assign_role_and_module, 
    approve_user, 
    create_role, 
    edit_role, 
    delete_user, 
    toggle_role_status, 
    create_module, 
    edit_module, 
    delete_module,
    add_permission,
    delete_permission
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'role_permissions', RolePermissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get_modules/', get_modules, name='get_modules'),
    path('get_roles_by_module/<int:module_id>/', get_roles_by_module, name='get_roles_by_module'),
    path('assign_role_and_module/<int:user_id>/', assign_role_and_module, name='assign_role_and_module'),
    path('approve_user/<int:user_id>/', approve_user, name='approve_user'),
    path('create_role/', create_role, name='create_role'),
    path('edit_role/<int:role_id>/', edit_role, name='edit_role'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path('toggle_role_status/<int:role_id>/', toggle_role_status, name='toggle_role_status'),
    path('create_module/', create_module, name='create_module'),
    path('edit_module/', edit_module, name='edit_module'),
    path('delete_module/<int:module_id>/', delete_module, name='delete_module'),
    path('add_permission/<int:role_id>/', add_permission, name='add_permission'),
    path('delete_permission/<int:permission_id>/', delete_permission, name='delete_permission'),
]
