from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import FrontendSpecificModelViewSet
from . import views as frontend_views

router = DefaultRouter()
router.register(r'frontend_model', FrontendSpecificModelViewSet, basename='frontend_model')

urlpatterns = [
    path('', include(router.urls)),
    path('send_verification_code/', frontend_views.send_verification_code, name='send_verification_code'),
    path('register/', frontend_views.register, name='register'),
]
