from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import BlogPostViewSet

app_name = 'blogs'

router = DefaultRouter()
router.register(r'blog', BlogPostViewSet, basename='blog')

urlpatterns = [
    path('', views.BlogPostListView, name='blog-view'),  # صفحه اصلی
    path('blog/<slug:slug>/', views.BlogPostDetailView, name='detail'),

    path('', include(router.urls)),

]
