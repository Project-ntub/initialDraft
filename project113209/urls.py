from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('frontend/', include('app113209.frontend.urls', namespace='frontend')),
    path('backend/', include('app113209.backend.urls', namespace='backend')),
    # path('account/', include(('two_factor.urls', 'two_factor'), namespace='two_factor')),
    # path('api/', include('app113209.api_urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/send_verification_code/', include('app113209.api_urls')),  # 确保这里的路径正确
]
