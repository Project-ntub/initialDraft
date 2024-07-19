# api_urls.py
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
]
