from djoser.serializers import UserSerializer, UserCreateSerializer as BaseUserSerializer
from django.core.exceptions import ValidationError


class UserCreateSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'email', 'gender', 'username', 'password']



class CurrentUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ['id', 'email', 'username']