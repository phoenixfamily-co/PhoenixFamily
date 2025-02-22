from PhoenixFamily import settings
from .models import SEOPage
from django.utils.translation import gettext_lazy as _


def seo_context(request):
    path = request.path.strip("/")  # گرفتن آدرس صفحه بدون دامنه
    seo_data = SEOPage.objects.prefetch_related('keywords').filter(page_url=path).first()

    if not seo_data:
        return {
            'seo_title': _(settings.SEO['default']['title']),
            'seo_description': _(settings.SEO['default']['description']),
            'seo_keywords': ", ".join([_(kw) for kw in settings.SEO['default']['keywords']]),  # تبدیل لیست به رشته
        }

    return {
        'seo_title': seo_data.title,
        'seo_description': seo_data.description,
        'seo_keywords': ", ".join([kw.name for kw in seo_data.keywords.all()]),  # دریافت کلمات کلیدی از مدل مرتبط
    }
