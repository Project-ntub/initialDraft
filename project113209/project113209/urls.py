from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('frontend/', include('app113209.frontend_urls', namespace='frontend')),
    path('backend/', include('app113209.backend_urls', namespace='backend')),
    path('account/', include(('two_factor.urls', 'two_factor'), namespace='two_factor')),
]
