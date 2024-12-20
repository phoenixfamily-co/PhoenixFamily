from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'blogs'

router = DefaultRouter()
router.register(r'blog', BlogPostViewSet, basename='blog')

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blog-view'),  # صفحه اصلی
    path('blog/<slug:slug>/', BlogPostDetailView.as_view(), name='detail'),

    path('', include(router.urls)),

]
