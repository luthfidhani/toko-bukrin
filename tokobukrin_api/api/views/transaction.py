from django.http.response import JsonResponse
from api.models import Transactions, Charts, ItemTransactions
from api.serializers import ItemTransactionSerializer, TransactionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .credit import checkSaldo, minusSaldo
from .auth import validation
from .chart import removeChart
from django.db import connection
import numpy as np
from uuid import uuid4


@api_view(["GET", "PUT", "DELETE", "POST"])
def transaction(request):
    if request.method == "POST":
        try:
            val = validation(request.data["token"])
            if val:
                if Charts.objects.filter(id_user=val["id_user"]):
                    query = "SELECT `api_items`.`id`, `api_items`.`name`, `api_charts`.`amount`, `api_items`.`price`, `api_items`.`discount`\
                        FROM `api_charts`\
                        INNER JOIN `api_items`\
                        ON(`api_charts`.`id_item_id`= `api_items`.`id`)\
                        WHERE `api_charts`.`id_user_id`='{}'".format(
                        val["id_user"].hex
                    )
                    cursor = connection.cursor()
                    cursor.execute(query)
                    row = cursor.fetchall()
                    amount_list = np.array([item[2] for item in row])
                    price_list = np.array([item[3] for item in row])
                    discount_list = np.array([item[4] for item in row])
                    all_total_price = np.sum(amount_list * (price_list - discount_list))

                    if (
                        request.data["payment"] == "saldo"
                        or request.data["payment"] == "cash"
                    ):
                        if request.data["payment"] == "saldo":
                            saldo = checkSaldo(val["id_user"])
                            if all_total_price >= saldo:
                                return Response(
                                    {
                                        "status": "error",
                                        "message": "Saldo tidak mencukupi",
                                    },
                                    status=status.HTTP_404_NOT_FOUND,
                                )
                            minusSaldo(val["id_user"], all_total_price)
                    else:
                        return Response(
                            {
                                "status": "error",
                                "message": "Metode salah (saldo / cash)",
                            },
                            status=status.HTTP_404_NOT_FOUND,
                        )

                    request.data._mutable = True
                    request.data["id"] = uuid4()
                    request.data["id_user"] = val["id_user"]
                    request.data._mutable = False
                    serializer = TransactionSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        for r in row:
                            data = {
                                "id_transaction": request.data["id"],
                                "id_item": r[0],
                                "name": r[1],
                                "amount": r[2],
                                "price": r[3],
                                "discount": r[4],
                                "total_price": r[2] * (r[3] - r[4]),
                            }
                            it_serialize = ItemTransactionSerializer(data=data)
                            if it_serialize.is_valid():
                                it_serialize.save()
                                removeChart(val["id_user"])
                            else:
                                return Response(it_serialize.errors)
                        return Response({"status": "Success"})
                    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
                return Response(
                    {"status": "error", "message": "Keranjang masih kosong"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            return Response(
                {"status": "error", "message": "Login terlebih dahulu"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"status": "error", "message": str(e)}, status=status.HTTP_404_NOT_FOUND
            )
