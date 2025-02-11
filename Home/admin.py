from django.contrib import admin
from translations import *
from modeltranslation.admin import TranslationAdmin
from .models import *


class ContentAdmin(TranslationAdmin):
    list_display = ('title', 'description')


admin.site.register(Content, ContentAdmin)


class VisionAdmin(TranslationAdmin):
    list_display = ('title', 'description')


admin.site.register(Vision, VisionAdmin)


class FeaturesAdmin(TranslationAdmin):
    list_display = ('title', 'description')


admin.site.register(Features, FeaturesAdmin)
