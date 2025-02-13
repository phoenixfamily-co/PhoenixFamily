from django.shortcuts import render
from django.utils.translation import get_language, get_language_bidi

from About.models import AboutUs
from Product.models import Product
from .serializers import ContentSerializer, FeaturesSerializer, VisionSerializer
from .models import Content, Vision, Features
from rest_framework import viewsets


def home(request):
    current_language = get_language()
    is_bidi = get_language_bidi()
    content = Content.objects.all()
    vision = Vision.objects.all()
    features = Features.objects.all()
    about = AboutUs.objects.first()
    products = Product.objects.all()

    return render(request, 'home.html',
                  {'LANGUAGE_CODE': current_language,
                   'LANGUAGE_BIDI': is_bidi,
                   'Content': content,
                   'Vision': vision,
                   'Features': features,
                   'About': about,
                   'Products': products,
                   },
                  )


# _____________________________ Class Based Views for developing API ________________________________

class ContentView(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class VisionView(viewsets.ModelViewSet):
    queryset = Vision.objects.all()
    serializer_class = VisionSerializer


class FeaturesView(viewsets.ModelViewSet):
    queryset = Features.objects.all()
    serializer_class = FeaturesSerializer
