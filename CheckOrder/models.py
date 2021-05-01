from django.db import models
from django.utils import timezone


# Create your models here.
#add order model
class Order(models.Model):
    Name=models.CharField(max_length=50)
    Goods_Name=models.CharField(max_length=50)
    Quantity=models.IntegerField()
    Order_Date=models.DateTimeField(default=timezone.now)
    Delivery_Date=models.DateField(blank=True,null=True)


    def __str__(self):
        return self.Name


#add delivery model
class Delivery(models.Model):
    Name=models.CharField(max_length=50)
    Goods_Name=models.CharField(max_length=50)
    Quantity=models.IntegerField()
    Order_Date=models.DateTimeField(blank=True,null=True)
    Delivery_Date=models.DateField(blank=True,null=True)

    def __str__(self):
        return self.Name
