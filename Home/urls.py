from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'content', views.ContentView)

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home-view'),  # صفحه اصلی
    path('api/', include(router.urls)),
]
