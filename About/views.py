from django.shortcuts import render
from django.utils.translation import get_language
from django.views.decorators.cache import cache_page
from rest_framework.viewsets import ModelViewSet
from .models import Us, FAQ
from .serializers import UsSerializer, FAQSerializer


@cache_page(60 * 15)
def about(request):
    current_language = get_language()
    return render(request, 'about.html', {'LANGUAGE_CODE': current_language})

# _____________________________ Class Based Views for developing API ________________________________

class UsCRUDView(ModelViewSet):
    queryset = Us.objects.all()
    serializer_class = UsSerializer


class FAQCRUDView(ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
