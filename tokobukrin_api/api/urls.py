from django.urls import path
from .views import item, user, auth, chart, transaction

urlpatterns = [
    path("item", item.item, name="item"),
    path("user", user.user, name="user"),
    path("auth", auth.login, name="login"),
    path("auth/logout", auth.logout, name="logout"),
    path("chart", chart.chart, name="chart"),
    path("transaction", transaction.transaction, name="transaction"),
]
