from django.urls import path
from .views import registration_api_view, confirm_api_view, login_api_view
urlpatterns = [
    path('users/register/', registration_api_view),
    path('users/confirm/', confirm_api_view),
    path('users/login/', login_api_view),
]