from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('cart',views.cart,name='cart'),
    path('remove_cart<int:id>',views.removecart,name='removecart'),
    path('remove_cart<int:id>',views.removecart,name='removecart'),
    path('add_qty/<int:id>',views.add_qty,name='add_qty'),
    path('sub_qty/<int:id>',views.sub_qty,name='sub_qty'),
    path('payment',views.payment,name='payment'),
]
