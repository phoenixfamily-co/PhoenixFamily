from django.shortcuts import render
from django.utils.translation import get_language


def products(request):
    current_language = get_language()
    return render(request, 'products.html', {'LANGUAGE_CODE': current_language})
