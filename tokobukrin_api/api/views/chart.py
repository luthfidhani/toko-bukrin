from django.http.response import JsonResponse
from api.models import Charts
from api.serializers import ChartSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .auth import validation
from django.db import connection
from django.db.models import F
import collections


def removeChart(id_user):
    Charts.objects.filter(id_user=id_user).delete()
    return True


@api_view(["GET", "PUT", "DELETE", "POST"])
def chart(request):
    if request.method == "POST":
        try:
            val = validation(request.data["token"])
            if val:
                request.data._mutable = True
                request.data["id_user"] = val["id_user"]
                request.data._mutable = True

                serializer = ChartSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"status": "Success"})
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
            return Response(
                {"status": "error", "message": "Login terlebih dahulu"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"status": "error", "message": str(e)}, status=status.HTTP_404_NOT_FOUND
            )

    if request.method == "DELETE":
        try:
            val = validation(request.data["token"])
            if val:
                Charts.objects.get(
                    id=request.data["id_chart"], id_user=val["id_user"]
                ).delete()
                return Response({"status": "success"})
            return Response(
                {"status": "error", "message": "Login terlebih dahulu"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"status": "error", "message": str(e)}, status=status.HTTP_404_NOT_FOUND
            )

    if request.method == "PUT":
        try:
            val = validation(request.data["token"])
            if val:
                if request.data["function"] == "plus":
                    Charts.objects.filter(id=request.data["id_chart"]).update(
                        amount=F("amount") + 1
                    )
                elif request.data["function"] == "min":
                    Charts.objects.filter(id=request.data["id_chart"]).update(
                        amount=F("amount") - 1
                    )
                    if (
                        Charts.objects.filter(id=request.data["id_chart"]).values(
                            "amount"
                        )[0]["amount"]
                        <= 0
                    ):
                        Charts.objects.get(id=request.data["id_chart"]).delete()
                        return Response({"status": "Success", "message": "Item kosong"})
                else:
                    return Response(
                        {"status": "error", "message": "Fungsi = plus or min"},
                        status=status.HTTP_404_NOT_FOUND,
                    )
                return Response({"status": "Success"})
            return Response(
                {"status": "error", "message": "Login terlebih dahulu"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"status": "error", "message": str(e)}, status=status.HTTP_404_NOT_FOUND
            )

    if request.method == "GET":
        try:
            val = validation(request.GET["token"])
            if val:
                query = "SELECT `api_items`.`id`, `api_items`.`name`, `api_charts`.`amount`, `api_items`.`price`, `api_items`.`discount`, `api_items`.`image`\
                        FROM `api_charts`\
                        INNER JOIN `api_items`\
                        ON(`api_charts`.`id_item_id`= `api_items`.`id`)\
                        WHERE `api_charts`.`id_user_id`='{}'".format(
                    val["id_user"].hex
                )
                cursor = connection.cursor()
                cursor.execute(query)
                row = cursor.fetchall()
                fect_list = []
                for r in row:
                    data = collections.OrderedDict()
                    data["id_item"] = r[0]
                    data["name"] = r[1]
                    data["amount"] = r[2]
                    data["price"] = r[3]
                    data["discount"] = r[4]
                    data["total_price"] = r[2] * (data["price"] - data["discount"])
                    data["image"] = r[5]
                    fect_list.append(data)

                return JsonResponse(fect_list, safe=False)
            return Response(
                {"status": "error", "message": "Login terlebih dahulu"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"status": "error", "message": str(e)}, status=status.HTTP_404_NOT_FOUND
            )
