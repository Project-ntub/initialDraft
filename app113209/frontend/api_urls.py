# app113209/frontend/api_urls.py
from django.urls import path
from .api_views import FrontendSpecificModelViewSet

urlpatterns = [
    path('frontend_view1/', FrontendSpecificModelViewSet.as_view({'get': 'list'}), name='frontend_view1'),
    path('frontend_view2/', FrontendSpecificModelViewSet.as_view({'get': 'retrieve'}), name='frontend_view2'),
]
