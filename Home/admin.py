from django.contrib import admin
from translations import *
from modeltranslation.admin import TranslationAdmin
from .models import Content, Vision, Features


class ContentAdmin(TranslationAdmin):
    list_display = ('title','description')


admin.site.register(Content, ContentAdmin)
