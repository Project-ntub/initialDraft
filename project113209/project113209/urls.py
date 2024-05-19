from django.contrib import admin
from django.urls import path
from app113209 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard),
    path('users/', views.user_list, name='user_list'),
    path('role/', views.role),
    path('history/', views.history),

]
