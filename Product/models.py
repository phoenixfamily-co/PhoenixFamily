from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    logo = models.FileField(upload_to='images/', null=True)
    image = models.FileField(upload_to='images/', null=True)
    video = models.FileField(upload_to='videos/', null=True)
    genre = models.TextField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    address = models.URLField(verbose_name="ادرس", blank=True, null=True)




