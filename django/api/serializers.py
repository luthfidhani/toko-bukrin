from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Users
        fields = ["name", "phone_number", "address", "email", "password"]


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Session
        fields = ["token", "id_user"]


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Items
        fields = ["name", "price", "discount", "image", "category"]
