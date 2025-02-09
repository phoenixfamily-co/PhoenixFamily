from django.urls import path, include
from .views import products, ProductView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product', ProductView, basename='product')

app_name = 'products'

urlpatterns = [
    path('', products, name='product-view'),  # صفحه اصلی
    path('api/', include(router.urls)),
]
