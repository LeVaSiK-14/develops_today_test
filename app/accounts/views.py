from rest_framework.viewsets import ModelViewSet

from django.contrib.auth import get_user_model

from app.accounts.serializers import UserSerializer
from app.accounts.mixins import (
                UserRegistration,
)

User = get_user_model()


class RegistrationAPIView(ModelViewSet, UserRegistration):
    queryset = User.objects.all()
    serializer_class = UserSerializer
