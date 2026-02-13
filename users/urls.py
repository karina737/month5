from django.urls import path
from .views import RegisterAPIView, ConfirmAPIView, LoginAPIView
urlpatterns = [
    path('users/register/', RegisterAPIView.as_view()),
    path('users/confirm/', ConfirmAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
]