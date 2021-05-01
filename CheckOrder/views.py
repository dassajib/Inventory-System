from django.shortcuts import render,HttpResponseRedirect, get_object_or_404
from .forms import OrderTable, DeliveryTable
from .models import Order, Delivery


# Create your views here.


#This function will add ans show order
def add_show_order(request):
    if request.method== 'POST':
        ob = OrderTable(request.POST)
        if ob.is_valid():
            nm = ob.cleaned_data['Name']
            gn = ob.cleaned_data['Goods_Name']
            qu = ob.cleaned_data['Quantity']
            od = ob.cleaned_data['Order_Date']
            dd = ob.cleaned_data['Delivery_Date']
            add = Order(Name=nm, Goods_Name=gn, Quantity=qu, Order_Date=od, Delivery_Date=dd)
            add.save()
            ob = OrderTable()

    else:
        ob = OrderTable()
    ViewOrder =Order.objects.all()
    return render(request, 'CheckOrder/addandshow.html', {'form':ob, 'view':ViewOrder})



#this function will update and Edit order
def update_order(request,id):
    if request.method == 'POST':
        up = Order.objects.get(id=id)
        ob = OrderTable(request.POST, instance=up)
        if ob.is_valid:
            ob.save()
    else:
        up = Order.objects.get(id=id)
        ob = OrderTable(instance=up)   
    return render(request, 'CheckOrder/update.html', {'form':ob})



#this function will delete order

def delete_order(request,id):
    if request.method == 'POST':
        dl = Order.objects.get(id=id)
        dl.delete()
        return HttpResponseRedirect('/')



#This function will add ans show delivery
def delivery_goods(request):
    if request.method== 'POST':
        ob2 = DeliveryTable(request.POST)
        if ob2.is_valid():
            nm2 = ob2.cleaned_data['Name']
            gn2 = ob2.cleaned_data['Goods_Name']
            qu2 = ob2.cleaned_data['Quantity']
            od2 = ob2.cleaned_data['Order_Date']
            dd2 = ob2.cleaned_data['Delivery_Date']
            add2 = Delivery(Name=nm2, Goods_Name=gn2, Quantity=qu2, Order_Date=od2, Delivery_Date=dd2)
            add2.save()
            ob2 = DeliveryTable()
    else:
        ob2 = DeliveryTable()
    ViewDelivery =Delivery.objects.all()
    return render(request, 'CheckOrder/delivery.html', {'form':ob2, 'view2':ViewDelivery})




#this function will update and Edit delivery
def update_delivery(request,id):
    if request.method == 'POST':
        up2 = get_object_or_404(Delivery,id=id)
        ob2 = DeliveryTable(request.POST, instance=up2)
        if ob2.is_valid:
            ob2.save()
    else:
        #up2 = Delivery.objects.get(id=id)
        ob2 = DeliveryTable(instance=up2)   
    return render(request, 'CheckOrder/update_delivery.html', {'form':ob2})




#this function will delete delivery

def delete_delivery(request,id):
    if request.method == 'POST':
        dl2 = Delivery.objects.get(id=id)
        dl2.delete()
        return HttpResponseRedirect('CheckOrder/delivery.html')