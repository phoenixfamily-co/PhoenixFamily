from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User  # برای مدیریت نویسنده‌ها


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)  # تاریخ انتشار
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")  # نویسنده مقاله
    category = models.CharField(max_length=100, blank=True, null=True)  # دسته‌بندی
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)  # تصویر شاخص
    meta_title = models.CharField(max_length=255, blank=True, null=True)  # عنوان برای SEO
    meta_description = models.CharField(max_length=160, blank=True, null=True)  # توضیحات برای SEO
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)  # کلمات کلیدی برای SEO

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            # اگر اسلاگ قبلاً وجود داشته باشد، یک پسوند اضافه کنید
            while BlogPost.objects.filter(slug=self.slug).exists():
                self.slug = f"{slugify(self.title)}-{self.id}"
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/blog/{self.slug}/"

    def __str__(self):
        return self.title
