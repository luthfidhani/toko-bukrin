from django.core import serializers
from api.models import Items
from api.serializers import ItemSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .auth import validation


@api_view(["GET", "PUT", "DELETE", "POST"])
def item(request):
    if request.method == "POST":
        try:
            val = validation(request.data["token"])
            if val["level"] == "admin":
                if request.POST["name"]:
                    serializer = ItemSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({"status": "Success"})
                return Response(
                    {"status": "error", "message": "Produk tidak boleh kosong"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            return Response(
                {"status": "error", "message": "Anda bukan admin"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except:
            return Response(
                {"status": "error", "message": "wupss!!"},
                status=status.HTTP_404_NOT_FOUND,
            )

    if request.method == "GET":
        if not request.GET:
            queryset = Items.objects.filter(is_delete=0)
            serializer = ItemSerializer(queryset, many=True)
            return Response(serializer.data)
        try:
            queryset = Items.objects.get(id=request.GET["id"], is_delete=0)
            serializer = ItemSerializer(queryset)
            return Response(serializer.data)
        except:
            return Response(
                {"status": "error", "message": "wupss!!"},
                status=status.HTTP_404_NOT_FOUND,
            )

    if request.method == "PUT":
        try:
            if validation(request.data["token"]) == "admin":
                try:
                    queryset = Items.objects.get(id=request.data["id"], is_delete=0)
                    serializer = ItemSerializer(queryset, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({"status": "Success"})
                    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
            return Response(
                {"status": "error", "message": "Anda bukan admin"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"status": "error", "message": "wupss!!"},
                status=status.HTTP_404_NOT_FOUND,
            )

    if request.method == "DELETE":
        try:
            if validation(request.data["token"]) == "admin":
                try:
                    queryset = Items.objects.get(id=request.data["id"], is_delete=0)
                    queryset.is_delete = 1
                    queryset.save()
                    return Response({"status": "Success"})
                except Exception as e:
                    print(e)
                    return Response(
                        {"status": "error", "message": "wupss!!"},
                        status=status.HTTP_404_NOT_FOUND,
                    )
            return Response(
                {"status": "error", "message": "Anda bukan admin"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"status": "error", "message": "wupss!!"},
                status=status.HTTP_404_NOT_FOUND,
            )
