from django.db import models
import uuid


class Users(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    credit = models.IntegerField(default=0)
    address = models.TextField()
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=0)
    is_delete = models.BooleanField(default=0)
    level = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Items(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=True)
    discount = models.IntegerField(default=0, null=True)
    image = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255, null=True)
    is_empty = models.BooleanField(default=0)
    is_delete = models.BooleanField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Topup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    amount = models.IntegerField()
    payment = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)


class Charts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    id_item = models.ForeignKey(Items, on_delete=models.CASCADE)
    amount = models.IntegerField()


class Transactions(models.Model):
    id = models.UUIDField(primary_key=True)
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    payment = models.CharField(max_length=10)
    shipment = models.CharField(max_length=10)
    message = models.TextField(null=True)
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)


class ItemTransactions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_transaction = models.ForeignKey(Transactions, on_delete=models.CASCADE)
    id_item = models.ForeignKey(Items, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    price = models.IntegerField(null=True)
    total_price = models.IntegerField(null=True)
    discount = models.IntegerField(default=0, null=True)
    amount = models.IntegerField(null=True)


class Session(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    token = models.UUIDField(null=True)
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    level = models.IntegerField(null=True)
    is_active = models.BooleanField(default=1)
    expired_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
