from .models import SEOPage


def seo_context(request):
    path = request.path.strip("/")  # گرفتن آدرس صفحه بدون دامنه
    seo_data = SEOPage.objects.filter(page=path).first()

    if not seo_data:
        seo_data = {
            'title': 'Default Title',
            'description': 'Default Description',
            'keywords': 'default, keywords'
        }

    return {
        'seo_title': getattr(seo_data, 'title', "Default Title"),
        'seo_description': getattr(seo_data, 'description', "Default Description"),
        'seo_keywords': getattr(seo_data, 'keywords', "default, keywords"),
    }
