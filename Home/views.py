from django.shortcuts import render
from django.utils.translation import get_language


def home(request):
    current_language = get_language()
    return render(request, 'home.html', {'LANGUAGE_CODE': current_language})
