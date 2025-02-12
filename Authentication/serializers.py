from rest_framework import serializers
from User.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['number', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        """Ensure passwords match and number is unique."""
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})

        if User.objects.filter(number=data['number']).exists():
            raise serializers.ValidationError({"number": "This phone number is already in use."})

        return data

    def create(self, validated_data):
        """Create a new user with `is_temporary=False`."""
        validated_data.pop('password2')  # Remove password2 since it's not in the model
        user = User.objects.create_user(
            number=validated_data['number'],
            password=validated_data['password'],
            is_temporary=False  # Ensure new users are not temporary
        )
        return user


class LoginSerializer(serializers.Serializer):
    number = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        """Authenticate user with phone number & password."""
        number = data.get('number')
        password = data.get('password')

        user = authenticate(username=number, password=password)

        if not user:
            raise serializers.ValidationError("Invalid phone number or password.")

        if not user.is_active:
            raise serializers.ValidationError("This account is inactive.")

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)

        return {
            "user_id": user.id,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        }