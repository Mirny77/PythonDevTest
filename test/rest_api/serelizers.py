from rest_framework import serializers
from django.contrib.auth.models import User

from contacts.models import NewContact


class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = User
        fields = ("id", "username")


class NewContactserializers(serializers.ModelSerializer):

    creater = UserSerializer()
    invited = UserSerializer(many=True)
    class Meta:
        model = NewContact
        fields = ("id", "user", "invited", )
