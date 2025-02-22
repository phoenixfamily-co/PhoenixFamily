from rest_framework import serializers
from .models import SEOPage


class SEOPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEOPage
        fields = ['page_url', 'title', 'description', 'keywords']
