from django.shortcuts import render
from django.utils.translation import get_language, get_language_bidi
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
def home(request):
    current_language = get_language()
    is_bidi = get_language_bidi()

    return render(request, 'home.html', {'LANGUAGE_CODE': current_language, 'LANGUAGE_BIDI': is_bidi})
