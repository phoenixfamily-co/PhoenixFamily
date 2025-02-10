from django.shortcuts import render
from django.utils.translation import get_language, get_language_bidi
from django.views.decorators.cache import cache_page
from rest_framework.viewsets import ModelViewSet

from About.models import AboutUs
from .models import Product, Features
from .serializers import ProductSerializer, FeaturesSerializer


@cache_page(60 * 15)
def products(request, pk):
    current_language = get_language()
    is_bidi = get_language_bidi()
    aboutUs = AboutUs.objects.first()
    product = Product.objects.all()
    item = Product.objects.get(id=pk)
    features = Features.objects.filter(product=pk)

    return render(request, 'products.html', {'LANGUAGE_CODE': current_language,
                                             'LANGUAGE_BIDI': is_bidi,
                                             'About': aboutUs,
                                             'Products': product,
                                             'Item': item,
                                             'Features': features
                                             })


# _____________________________ Class Based Views for developing API ________________________________

class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class FeaturesView(ModelViewSet):
    queryset = Features.objects.all()
    serializer_class = FeaturesSerializer
