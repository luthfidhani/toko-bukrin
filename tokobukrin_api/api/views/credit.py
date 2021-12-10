from api.models import Users
from django.db.models import F


def checkSaldo(id_user):
    saldo = Users.objects.filter(id=id_user).values("credit")
    return saldo[0]["credit"]


def minusSaldo(id_user, bayar):
    Users.objects.filter(id=id_user).update(credit=F("credit") - bayar)
    return True
