from rest_framework import serializers
from django.contrib.auth import get_user_model
from .services.user_service import create_user

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            'degree',
            'year_joined',
            'role',
        )

    def create(self, validated_data):
        return create_user(validated_data)
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)