from django.shortcuts import render
from django.utils.translation import get_language
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
def about(request):
    current_language = get_language()
    return render(request, 'about.html', {'LANGUAGE_CODE': current_language})
