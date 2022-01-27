from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.status import (
                HTTP_400_BAD_REQUEST,
                HTTP_201_CREATED
)

from django.contrib.auth import get_user_model

from app.accounts.serializers import (
                RegistrationSerializer,
)

User = get_user_model()


class UserRegistration:

    @action(methods=['post', ], detail=False, serializer_class=RegistrationSerializer)
    def registration(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({'Message': 'User with such username is already exists'}, status=HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=username,
            password=password
        )

        token = Token.objects.create(user=user)

        return Response({'token': token.key}, status=HTTP_201_CREATED)
