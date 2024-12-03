from rest_framework import serializers
from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()  # نمایش نام نویسنده به جای ID
    published_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title",
            "slug",
            "content",
            "published_date",
            "author",
            "category",
            "image",
            "meta_title",
            "meta_description",
            "meta_keywords",
        ]
