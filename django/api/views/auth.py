# from api.models import Users, Session
# from django.contrib.auth.hashers import check_password, make_password
# from uuid import uuid4
# from api import forms
# from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
# def login(request):
#     if not (request.POST['email'] and request.POST['password']):
#         data = {
#             'status': 'error',
#             'message': 'Email Password tidak boleh kosong'
#         }
#         return data

#     obj = Users.objects.filter(
#         email=request.POST['email']).values_list('id', 'password')
#     id_user = obj[0][0]
#     password_user = obj[0][1]
#     if not obj:
#         data = {
#             'status': 'error',
#             'message': 'User tidak ditemukan'
#         }
#         return data
#     if not check_password(request.POST['password'], password_user):
#         data = {
#             'status': 'error',
#             'message': 'User tidak ditemukan'
#         }
#         return data

#     rand_token = uuid4()
#     field = {
#         'id_user': id_user,
#         'token': rand_token
#     }
#     form = forms.AuthForm(field)
#     form.save()
#     data = {
#         'status': 'success',
#         'data': {
#             'id_user': id_user,
#             'token': rand_token
#         }
#     }
#     return data


# @csrf_exempt
# def validation(request):
#     if not (request.POST['id_user'] and request.POST['token']):
#         data = {
#             'status': 'error',
#             'message': 'id_user token tidak boleh kosong'
#         }
#         return data
#     try:
#         obj = Session.objects.filter(
#             id_user=request.POST['id_user'], token=request.POST['token'], is_active=1)
#         if not obj:
#             data = {
#                 'status': 'error',
#                 'message': 'Session tidak aktif'
#             }
#             return data
#         data = {
#             'status': 'success',
#             'message': 'Session aktif'

#         }
#         return data
#     except:
#         data = {
#             'status': 'error',
#             'message': 'Session tidak aktif'
#         }
#         return data
