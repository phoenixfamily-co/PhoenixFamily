from rest_framework import serializers
from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()  # نمایش نام نویسنده به جای ID

    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title",
            "slug",
            "content",
            "author",
            "image",
            "meta_title",
            "meta_description",
            "meta_keywords",
        ]
