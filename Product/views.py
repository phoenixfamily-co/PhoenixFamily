from django.shortcuts import render
from django.utils.translation import get_language, get_language_bidi
from django.views.decorators.cache import cache_page
from rest_framework.viewsets import ModelViewSet

from About.models import AboutUs
from .models import Product
from .serializers import ProductSerializer


@cache_page(60 * 15)
def products(request, pk):
    current_language = get_language()
    is_bidi = get_language_bidi()
    aboutUs = AboutUs.objects.first()
    product = Product.objects.all()

    return render(request, 'products.html', {'LANGUAGE_CODE': current_language,
                                             'LANGUAGE_BIDI': is_bidi,
                                             'AboutUs': aboutUs,
                                             'Products': product,
                                             })


# _____________________________ Class Based Views for developing API ________________________________

class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
