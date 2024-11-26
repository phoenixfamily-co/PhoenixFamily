from django.shortcuts import render
from django.utils.translation import get_language


def blogs(request):
    current_language = get_language()
    return render(request, 'blogs.html', {'LANGUAGE_CODE': current_language})
