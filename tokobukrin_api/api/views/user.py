from django.core import serializers
from api.models import Users, Session
from api.serializers import UserSerializer, GetUserSerializer, EditUserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .auth import validation


@api_view(["GET", "PUT", "DELETE", "POST"])
def user(request):
    # Register
    if request.method == "POST":
        try:
            if request.POST["password"] == request.POST["password_confirm"]:
                has_user = Users.objects.filter(
                    email=request.POST["email"], is_delete=0
                )
                if has_user:
                    return Response(
                        {"status": "error", "message": "Email sudah digunakan"},
                        status=status.HTTP_404_NOT_FOUND,
                    )

                request.POST._mutable = True
                request.POST["password"] = make_password(request.POST["password"])
                request.POST._mutable = False
                serializer = UserSerializer(data=request.POST)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"status": "Success"})
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
            return Response(
                {"status": "error", "message": "password tidak sama"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except:
            return Response(
                {"status": "error", "message": "wupss!!"},
                status=status.HTTP_404_NOT_FOUND,
            )

    # Get user
    if request.method == "GET":
        try:
            val = validation(request.GET["token"])
            if val:
                queryset = Users.objects.get(id=val["id_user"], is_delete=0)
                if queryset:
                    serializer = GetUserSerializer(queryset)
                    return Response(serializer.data)
            return Response(
                {"status": "error", "message": "User tidak ditemukan"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except:
            return Response(
                {"status": "error", "message": "Login terlebih dahulu"},
                status=status.HTTP_404_NOT_FOUND,
            )

    # Edit user
    if request.method == "PUT":
        try:
            val = validation(request.data["token"])
            if val:
                queryset = Users.objects.get(id=val["id_user"], is_delete=0)
                serializer = EditUserSerializer(queryset, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"status": "Success"})
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
            return Response(
                {"status": "error", "message": "User tidak ditemukan"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except:
            return Response(
                {"status": "error", "message": "Login terlebih dahulu"},
                status=status.HTTP_404_NOT_FOUND,
            )

    # Edit delete user
    if request.method == "DELETE":
        try:
            val = validation(request.data["token"])
            if val:
                Session.objects.filter(id_user=val["id_user"], is_active=1).update(
                    is_active=0
                )
                queryset = Users.objects.get(id=val["id_user"], is_delete=0)
                queryset.is_delete = 1
                queryset.save()
                return Response({"status": "Success"})

            return Response(
                {"status": "error", "message": "User tidak ditemukan"},
                status=status.HTTP_404_NOT_FOUND,
            )

        except Exception as e:
            print(e)
            return Response(
                {"status": "error", "message": "Login terlebih dahulu"},
                status=status.HTTP_404_NOT_FOUND,
            )
