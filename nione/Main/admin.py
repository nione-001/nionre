from django.contrib import admin
from .models import *

admin.site.register(Account)
admin.site.register(ForgetPass)
admin.site.register(Hotel)
admin.site.register(CurrentOrders)
admin.site.register(FinishedOrders)
admin.site.register(Subscription)
admin.site.register(HotelOwner)
admin.site.register(AutoMate)

