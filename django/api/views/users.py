# from django.http.response import JsonResponse
# from django.core import serializers
# from api.models import Users
# from django.contrib.auth.hashers import check_password, make_password

# from api import forms
# from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
# def register(request):
#     form = forms.UserForm(request.POST)
#     if form.is_valid():
#         if Users.objects.filter(email=request.POST['email']):
#             data = {
#                 'status': 'error',
#                 'message': 'Email sudah terdaftar'
#             }
#             return data

#         if request.POST['password'] != request.POST['confirm_password']:
#             data = {
#                 'status': 'error',
#                 'message': 'Password tidak sama'
#             }
#             return data

#         request.POST._mutable = True
#         request.POST['password'] = make_password(request.POST['password'])
#         request.POST._mutable = False

#         form = forms.UserForm(request.POST)
#         form.save()
#         data = {
#             'status': 'success'
#         }
#         return data

#     data = {
#         'status': 'error',
#         'message': 'Data tidak terisi penuh'
#     }
#     return data


# @csrf_exempt
# def getUser(request):
#     user = Users.objects.filter(id=request.POST['id']).values_list(
#         'name', 'phone_number', 'credit', 'address', 'email', 'is_active')
#     if user:
#         data = {
#             'status': 'success',
#             'data': {
#                 'name': user[0][0],
#                 'phone_number': user[0][1],
#                 'credit': user[0][2],
#                 'address': user[0][3],
#                 'email': user[0][4],
#                 'is_active': user[0][5],
#             }
#         }
#         return data
#     data = {
#         'status': 'error',
#         'message': 'User tidak ditemukan'
#     }
#     return data


# @csrf_exempt
# def update(request):
#     try:
#         obj = Users.objects.get(id=request.POST['id'])
#         if obj:
#             obj.name = request.POST['name']
#             obj.phone_number = request.POST['phone_number']
#             obj.address = request.POST['address']
#             obj.email = request.POST['email']
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
#             'message': 'User tidak ditemukan'
#         }
#         return data


# @csrf_exempt
# def resetPassword(request):
#     if request.POST['new_password'] != request.POST['confirm_password']:
#         data = {
#             'status': 'error',
#             'message': 'Password tidak sama'
#         }
#         return data
#     try:
#         obj = Users.objects.get(
#             id=request.POST['id'])
#         if check_password(request.POST['password'], obj.password):
#             obj.password = make_password(request.POST['new_password'])
#             obj.save()
#             data = {
#                 'status': 'success',
#                 'message': 'Password berhasil diupdate'
#             }
#             return data
#         data = {
#             'status': 'error',
#             'message': 'User tidak ditemukan'
#         }
#         return data
#     except Exception as e:
#         print(e)
#         data = {
#             'status': 'error',
#             'message': 'User tidak ditemukan'
#         }
#         return data
