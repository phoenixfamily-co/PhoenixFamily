from django.contrib.sitemaps import Sitemap
from django.utils.translation import activate

from .models import BlogPost
from django.urls import reverse


class BlogPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return BlogPost.objects.all()

    def location(self, obj):
        activate(obj.language)
        # برای هر زبان نقشه‌های جداگانه بسازید
        return reverse('blogs:detail', kwargs={'slug': obj.slug})



