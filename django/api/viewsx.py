from api.table import users, auth, item
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.http import QueryDict
from rest_framework import viewsets


# class User():
#     @csrf_exempt
#     def register(request):
#         data = users.register(request)
#         return JsonResponse(data)

#     @csrf_exempt
#     def getUser(request):
#         data = users.getUser(request)
#         return JsonResponse(data)

#     @csrf_exempt
#     def update(request):
#         data = users.update(request)
#         return JsonResponse(data)

#     @csrf_exempt
#     def resetPassword(request):
#         data = users.resetPassword(request)
#         return JsonResponse(data)


# class Auth():
#     @csrf_exempt
#     def login(request):
#         data = auth.login(request)
#         return JsonResponse(data)

#     @csrf_exempt
#     def validation(request):
#         data = auth.validation(request)
#         return JsonResponse(data)


# class Item():
#     @csrf_exempt
#     class show(viewsets.ModelViewSet):
#         item.Show(viewsets.ModelViewSet)
# return JsonResponse(data)

# @csrf_exempt
# class add(viewsets.ModelViewSet):
#     data = item.add(viewsets.ModelViewSet)
#     # return JsonResponse(data)

# @csrf_exempt
# class edit(viewsets.ModelViewSet):
#     data = item.edit(viewsets.ModelViewSet)
#     # return JsonResponse(data)
