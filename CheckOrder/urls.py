from django.urls import path
from . import views 

urlpatterns = [
    #path('', views.add_show_order, name="order"),
    #path('order/<int:id>', views.delete_order, name="delete"),
    #path('order/<int:id>/', views.update_order, name="update"),
    path('delivery/', views.delivery_goods, name="delivery"),
    path('delivery/<int:id>/', views.delete_delivery, name="delete_delivery"),
    path('delivery/<int:id>/', views.update_delivery, name="update_delivery"),
]