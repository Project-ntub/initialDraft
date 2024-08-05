from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('app113209.urls')),
    path('api/', include(('app113209.backend.api_urls', 'backend_api'), namespace='backend_api')),
    path('frontend/', include(('app113209.frontend.urls', 'frontend'), namespace='frontend')),
    path('backend/', include(('app113209.backend.urls', 'backend'), namespace='backend')),
    # path('account/', include('two_factor.urls', namespace='two_factor')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/send_verification_code/', include('app113209.frontend.api_urls')),  # 确保这里的路径正确
]
