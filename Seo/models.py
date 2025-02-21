from django.db import models


class SEOPage(models.Model):
    page_url = models.CharField(max_length=255, unique=True, help_text="مسیر صفحه بدون دامنه، مثل /about/")
    title = models.CharField(max_length=255, help_text="عنوان صفحه (Title)")
    description = models.TextField(help_text="توضیحات متا (Meta Description)")
    keywords = models.CharField(max_length=500, blank=True, help_text="کلمات کلیدی (Keywords)")

    def __str__(self):
        return self.title
