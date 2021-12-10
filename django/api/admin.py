from django.contrib import admin
from .models import Users, Items, Topup, Charts, Transactions, ItemTransactions, Session

admin.site.register(Users)
admin.site.register(Items)
admin.site.register(Topup)
admin.site.register(Charts)
admin.site.register(Transactions)
admin.site.register(ItemTransactions)
admin.site.register(Session)
