from django.contrib import admin
from .models import SEOPage


@admin.register(SEOPage)
class SEOPageAdmin(admin.ModelAdmin):
    list_display = ('page_url', 'title', 'description')
    search_fields = ('page_url', 'title')
