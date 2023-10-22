from django.shortcuts import render,redirect
from django.contrib import messages
from products.models import Product
from .models import Order,OrderDetails
from django.utils import timezone


def add_to_cart(request):
    if 'product_id' in request.GET and 'quantity' in request.GET and 'price' in request.GET and request.user.is_authenticated and not request.user.is_anonymous:
        product_id = request.GET['product_id']
        quantity = request.GET['quantity']
        order = Order.objects.all().filter(user=request.user,is_finished=False)
        if not Product.objects.all().filter(id=product_id).exists():
            return redirect('products')
        product = Product.objects.get(id=product_id)
        if order:
            messages.success(request,'Find old order')
            old_order = Order.objects.get(user=request.user,is_finished=False)
            orderdetails = OrderDetails.objects.create(product=product,order=old_order,quantity=quantity)
            messages.success(request,'was added to cart for old orders')
        else:
            messages.success(request,'Run new order')
            new_order = Order()
            new_order.user = request.user
            new_order.created_at = timezone.now()
            new_order.is_finished = False
            new_order.save()
            orderdetails = OrderDetails.objects.create(product=product,order=new_order,price=product.price,quantity=quantity)
            messages.success(request,'added to new order')
        return redirect('/products/' + request.GET['product_id'])
    else:
        return redirect('products')