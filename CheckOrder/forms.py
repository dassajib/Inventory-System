from django import forms
from .models import Order, Delivery

class OrderTable(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['Name' ,'Goods_Name', 'Quantity', 'Order_Date', 'Delivery_Date']
      

class DeliveryTable(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['Name', 'Goods_Name', 'Quantity', 'Order_Date', 'Delivery_Date']