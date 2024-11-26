from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.products, name='product-view'),  # صفحه اصلی
]
