from django.shortcuts import render
from django.utils.translation import get_language, get_language_bidi
from django.views.decorators.cache import cache_page
from rest_framework.viewsets import ModelViewSet
from .models import AboutUs, FAQ
from .serializers import AboutUsSerializer, FAQSerializer


@cache_page(60 * 15)
def about(request):
    current_language = get_language()
    is_bidi = get_language_bidi()

    aboutUs = AboutUs.objects.first()
    faq = FAQ.objects.all()

    return render(request, 'about.html', {'LANGUAGE_CODE': current_language,
                                          'LANGUAGE_BIDI': is_bidi,
                                          'AboutUs': aboutUs,
                                          'FAQ': faq
                                          })

# _____________________________ Class Based Views for developing API ________________________________


class AboutUsView(ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class FAQView(ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
