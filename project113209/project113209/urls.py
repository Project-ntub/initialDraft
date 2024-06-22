from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # 后台管理界面
    path('frontend/', include('app113209.frontend_urls')),  # 前台
    path('backend/', include('app113209.backend_urls')),  # 后台
]
