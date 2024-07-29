from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import (
    UserViewSet, ModuleViewSet, RoleViewSet, RolePermissionViewSet,
    RoleListCreateView, RoleRetrieveUpdateDestroyView,
    RolePermissionListCreateView, RolePermissionRetrieveUpdateDestroyView,
    ModuleListCreateView, ModuleRetrieveUpdateDestroyView
)
 

# 設置API路由
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'role_permissions', RolePermissionViewSet)

# API 路由
api_urlpatterns = [
    path('', include(router.urls)),
    path('create_role/', RoleViewSet.as_view({'post': 'create'}), name='create_role'),
    path('create_module/', ModuleViewSet.as_view({'post': 'create'}), name='create_module'),
    path('toggle_role_status/<int:pk>/', RoleViewSet.as_view({'post': 'toggle_status'}), name='toggle_role_status'),
    path('delete_role/<int:role_id>/', RoleViewSet.as_view({'post': 'delete'}), name='delete_role'),
    path('get_modules/', ModuleViewSet.as_view({'get': 'get_modules'}), name='get_modules'),
    path('get_roles_by_module/<int:pk>/', RoleViewSet.as_view({'get': 'get_roles_by_module'}), name='get_roles_by_module'),
    path('assign_role_and_module/<int:user_id>/', UserViewSet.as_view({'post': 'assign_role_and_module'}), name='assign_role_and_module'),
    path('get_role_users/', UserViewSet.as_view({'get': 'get_role_users'}), name='get_role_users'),
    path('roles/', RoleListCreateView.as_view(), name='role-list-create'),
    path('roles/<int:pk>/', RoleRetrieveUpdateDestroyView.as_view(), name='role-retrieve-update-destroy'),
    path('role_permissions/', RolePermissionListCreateView.as_view(), name='role-permission-list-create'),
    path('role_permissions/<int:pk>/', RolePermissionRetrieveUpdateDestroyView.as_view(), name='role-permission-retrieve-update-destroy'),
    path('modules/', ModuleListCreateView.as_view(), name='module-list-create'),
    path('modules/<int:pk>/', ModuleRetrieveUpdateDestroyView.as_view(), name='module-retrieve-update-destroy'),
]

urlpatterns = api_urlpatterns
