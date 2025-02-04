from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

