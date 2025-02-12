from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView

app_name = "user"

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
]
