from django.urls import path
from .views import item

urlpatterns = [
    # path('user', views.User.getUser, name='getUser'),
    # path('user/register', views.User.register, name='register'),
    # path('user/update', views.User.update, name='update'),
    # path('user/resetPassword', views.User.resetPassword, name='resetPassword'),
    # path('auth', views.Auth.login, name='login'),
    # path('auth/validation', views.Auth.validation, name='validation'),
    path("item", item.Show, name="show"),
    # path('item/add', views.Item.add, name='add'),
    # path('item/edit', views.Item.edit, name='edit'),
]
