from django.db import models


# Create your models here.

class FAQ(models.Model):
    icon = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class AboutUs(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    linkedin = models.URLField(verbose_name="linkedin", blank=True, null=True)
    instagram = models.URLField(verbose_name="instagram", blank=True, null=True)
    whatsApp = models.URLField(verbose_name="whatsApp", blank=True, null=True)
    telegram = models.URLField(verbose_name="telegram", blank=True, null=True)
    logo = models.FileField(upload_to='images/', null=True)
    image = models.FileField(upload_to='images/', null=True)
    video = models.FileField(upload_to='videos/', null=True)
    alt = models.CharField(max_length=255, null=True, blank=True)
    context = models.TextField(blank=True, null=True)


