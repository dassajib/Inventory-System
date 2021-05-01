from django.contrib import admin
from .models import Order
from .models import Delivery 


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('id', 'Name', 'Goods_Name', 'Quantity', 'Order_Date', 'Delivery_Date',)


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display=('id', 'Name', 'Goods_Name', 'Quantity', 'Order_Date', 'Delivery_Date',)
    