import uuid
from django.core import serializers
from rest_framework import response
from api.models import Users, Session
from api.serializers import AuthSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import (
    UNUSABLE_PASSWORD_SUFFIX_LENGTH,
    make_password,
    check_password,
)
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from uuid import uuid4


def validation(token):
    try:
        session = Session.objects.filter(token=token, is_active=1).values(
            "level", "id_user"
        )
        if session[0]["level"] == 0:
            return {"level": "client", "id_user": session[0]["id_user"]}
        elif session[0]["level"] == 1:
            return {"level": "admin", "id_user": session[0]["id_user"]}
        else:
            return False
    except:
        return False


@api_view(["GET", "PUT", "DELETE", "POST"])
def login(request):
    if request.method == "POST":
        if request.POST["email"] and request.POST["password"]:
            user = Users.objects.filter(
                email=request.POST["email"], is_delete=0
            ).values_list("id", "email", "password", "level")
            if user:
                id_user = user[0][0]
                email_user = user[0][1]
                password_user = user[0][2]
                level = user[0][3]
                if check_password(request.POST["password"], password_user):
                    request.POST._mutable = True
                    request.POST.pop("email")
                    request.POST.pop("password")
                    request.POST["id"] = uuid4()
                    request.POST["token"] = uuid4()
                    request.POST["id_user"] = id_user
                    request.POST["level"] = level
                    request.POST._mutable = False

                    serializer = AuthSerializer(data=request.POST)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(request.POST)
                    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        return Response(
            {"status": "error", "message": "User tidak ditemukan"},
            status=status.HTTP_404_NOT_FOUND,
        )
    return Response({"status": "error"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET", "PUT", "DELETE", "POST"])
def logout(request):
    if request.method == "POST":
        if validation(request.POST["token"]):
            validation(request.POST["token"])
            Session.objects.filter(token=request.POST["token"], is_active=1).update(
                is_active=0
            )
            return Response({"status": "success"})
        return Response(
            {"status": "error", "message": "User tidak ditemukan"},
            status=status.HTTP_404_NOT_FOUND,
        )
    return Response({"status": "error"}, status=status.HTTP_404_NOT_FOUND)
