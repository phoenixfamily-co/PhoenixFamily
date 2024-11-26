from django.shortcuts import render
from django.utils.translation import get_language


def contact(request):
    current_language = get_language()
    return render(request, 'contact.html', {'LANGUAGE_CODE': current_language})
