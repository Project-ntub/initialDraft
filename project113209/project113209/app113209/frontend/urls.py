# frontend/urls.py
from django.urls import path
from . import views
# from .views import get_branch_chart_data
app_name = 'frontend'

urlpatterns = [
    path('send_verification_code/', views.send_verification_code, name='send_verification_code'),
    path('register/', views.register, name='register'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password/<str:token>/', views.reset_password, name='reset_password'),
    # path('get_branch_chart_data/<int:branch_id>/', get_branch_chart_data, name='get_branch_chart_data'),
]




