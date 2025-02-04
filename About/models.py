from django.db import models

# Create your models here.

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()


class Us(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=11)
    email = models.EmailField(blank=True, null=True)
    linkedin = models.URLField(verbose_name="linkedin", blank=True, null=True)
