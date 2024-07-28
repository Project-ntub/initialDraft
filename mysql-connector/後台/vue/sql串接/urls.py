from django.urls import path
from .views import get_user_profile, update_user_profile

urlpatterns = [
    path('user/<int:user_id>/', get_user_profile, name='get_user_profile'),
    path('user/update/<int:user_id>/', update_user_profile, name='update_user_profile'),
]
