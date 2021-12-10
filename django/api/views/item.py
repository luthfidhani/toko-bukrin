from rest_framework import status
from django.core import serializers
from api.models import Items
from api import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets


class Show(viewsets.ModelViewSet):
    print("weqwedwexcwecwexwc")
    queryset = Items.objects.all()
    serializer_class = serializers.ItemSerializer


# @csrf_exempt
# def add(request):
#     form = forms.ItemForm(request.POST)
#     if not form.is_valid():
#         data = {
#             'status': 'error',
#             'message': 'Data tidak lengkap'
#         }
#         return data

#     form.save()
#     data = {
#         'status': 'success'
#     }
#     return data


# @csrf_exempt
# def edit(request):
#     try:
#         obj = Items.objects.get(id=request.POST['id'])
#         if obj:
#             obj.name = request.POST['name']
#             obj.price = request.POST['price']
#             obj.discount = request.POST['discount']
#             obj.image = request.POST['image']
#             obj.category = request.POST['category']
#             obj.save()
#             data = {
#                 'status': 'success',
#                 'message': 'Data berhasil diupdate'
#             }
#             return data
#     except Exception as e:
#         print(e)
#         data = {
#             'status': 'error',
#             'message': 'Item tidak ditemukan'
#         }
#         return data
