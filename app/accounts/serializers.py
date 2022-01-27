from rest_framework import serializers, exceptions
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username'
        ]

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validated_password(self, value):
        if len(value) < 5:
            raise exceptions.ValidationError('Password is too short')
        elif len(value) > 20:
            raise exceptions.ValidationError('Password is too long')
        return value
