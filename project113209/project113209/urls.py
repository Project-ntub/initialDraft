from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('frontend/', include('app113209.frontend.urls', namespace='frontend')),
    path('backend/', include('app113209.backend.urls', namespace='backend')),
    path('account/', include(('two_factor.urls', 'two_factor'), namespace='two_factor')),
    # path('api/frontend/', include('app113209.frontend.api_urls')),
    path('api/backend/', include('app113209.backend.api_urls')),  # 添加命名空間
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
