from django.contrib import admin
from translations import *
from modeltranslation.admin import TranslationAdmin
from .models import *


class AboutUsAdmin(TranslationAdmin):
    list_display = ('title', 'description', 'name', 'alt', 'context')


admin.site.register(AboutUs, AboutUsAdmin)


class FAQAdmin(TranslationAdmin):
    list_display = ('title', 'description')


admin.site.register(FAQ, FAQAdmin)
