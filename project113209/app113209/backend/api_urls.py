from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import UserViewSet, ModuleViewSet, RoleViewSet, RolePermissionViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'role_permissions', RolePermissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create_role/', RoleViewSet.as_view({'post': 'create'}), name='create_role'),
    path('create_module/', ModuleViewSet.as_view({'post': 'create'}), name='create_module'),
    path('toggle_role_status/<int:pk>/', RoleViewSet.as_view({'post': 'toggle_status'}), name='toggle_role_status'),
    path('delete_role/<int:pk>/', RoleViewSet.as_view({'post': 'destroy'}), name='delete_role'),  # Ensure this line is correct
]
