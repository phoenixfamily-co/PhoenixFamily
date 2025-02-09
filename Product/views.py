import pickle

from django.shortcuts import render
from django.utils.translation import get_language
from django.views.decorators.cache import cache_page
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer


@cache_page(60 * 15)
def products(request, pk):
    current_language = get_language()
    return render(request, 'products.html', {'LANGUAGE_CODE': current_language})


# _____________________________ Class Based Views for developing API ________________________________

class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
