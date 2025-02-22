from PhoenixFamily import settings
from .models import SEOPage
from django.utils.translation import gettext_lazy as _


def seo_context(request):
    path = request.path.strip("/")  # گرفتن آدرس صفحه بدون دامنه
    seo_data = SEOPage.objects.filter(page=path).first()

    if not seo_data:
        return {
            'seo_title': _(settings.SEO['default']['title']),
            'seo_description': _(settings.SEO['default']['description']),
            'seo_keywords': ", ".join([_(kw) for kw in settings.SEO['default']['keywords']]),  # تبدیل لیست به استرینگ
        }

    return {
        'seo_title': seo_data.title,
        'seo_description': seo_data.description,
        'seo_keywords': seo_data.keywords,
    }
