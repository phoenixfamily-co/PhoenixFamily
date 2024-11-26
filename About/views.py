from django.shortcuts import render
from django.utils.translation import get_language


def about(request):
    current_language = get_language()
    return render(request, 'about.html', {'LANGUAGE_CODE': current_language})
