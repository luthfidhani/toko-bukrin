from django.db.models import fields
from rest_framework import serializers
from . import models


class GetUserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = models.Users
        fields = [
            "id",
            "name",
            "phone_number",
            "credit",
            "address",
            "email",
            "is_active",
            "created_at",
            "level",
        ]


class EditUserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = models.Users
        fields = ["id", "name", "phone_number", "address"]


class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = models.Users
        fields = [
            "id",
            "name",
            "phone_number",
            "credit",
            "address",
            "email",
            "is_active",
            "created_at",
            "password",
        ]


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Session
        fields = ["id", "token", "id_user", "level"]


class ItemSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = models.Items
        fields = ["id", "name", "price", "discount", "image", "category", "is_empty"]


class ChartSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = models.Charts
        fields = ["id", "id_item", "id_user", "amount"]


class GetChartSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=True)

    class Meta:
        fields = ["name", "price", "discount", "amount", "image"]


class TransactionSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = models.Transactions
        fields = [
            "id",
            "id_user",
            "payment",
            "shipment",
            "status",
            "message",
            "created_at",
        ]


class ItemTransactionSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = models.ItemTransactions
        fields = [
            "id",
            "id_transaction",
            "id_item",
            "name",
            "amount",
            "discount",
            "price",
            "total_price",
        ]
