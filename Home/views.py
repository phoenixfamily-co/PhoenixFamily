from django.shortcuts import render
from django.utils.translation import get_language, get_language_bidi
from .serializers import ContentSerializer
from .models import Content
from rest_framework import viewsets


def home(request):
    current_language = get_language()
    is_bidi = get_language_bidi()

    return render(request, 'home.html', {'LANGUAGE_CODE': current_language, 'LANGUAGE_BIDI': is_bidi})


# _____________________________ Class Based Views for developing API ________________________________

class ContentView(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
