from django.urls import path
from . import frontend_views

urlpatterns = [
    path('login/', frontend_views.FrontendLoginView.as_view(), name='frontend-login'),
    path('home/', frontend_views.home, name='frontend-home'),
]
