from django.shortcuts import render,get_object_or_404
from .models import Product

# Create your views here.

def products(request):
    items = {
        'products' : Product.objects.all()
    }
    return render(request,'products/products.html',items )


def product(request,product_id):
    item = {
        'product':get_object_or_404(Product,pk=product_id)
    }
    return render(request,'products/product.html',item)


def search(request):
    return render(request,'products/search.html')