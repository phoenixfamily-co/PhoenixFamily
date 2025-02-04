from django.db import models


# Create your models here.


class Content(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    video = models.FileField(upload_to='videos_uploaded', null=True)
