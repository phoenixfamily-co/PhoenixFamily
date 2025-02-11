from modeltranslation.translator import translator, TranslationOptions
from .models import Content, Vision, Features


class ContentTranslationOptions(TranslationOptions):
    fields = ('title', 'description')  # فیلدهایی که باید ترجمه شوند


translator.register(Content, ContentTranslationOptions)
