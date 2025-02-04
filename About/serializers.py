from rest_framework import serializers
from .models import Us, FAQ

class UsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Us
        fields = "__all__"


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"
