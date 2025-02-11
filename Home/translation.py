from modeltranslation.translator import translator, TranslationOptions
from .models import Content  # مدل را ایمپورت کنید


class ContentTranslationOptions(TranslationOptions):
    fields = ('title', 'description')  # فیلدهایی که باید ترجمه شوند


translator.register(Content, ContentTranslationOptions)  # ثبت مدل برای ترجمه
