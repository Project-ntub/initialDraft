from django.contrib import admin
from django.urls import path
from app113209.views import CustomLoginView, CustomLogoutView, register_view, 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
]
