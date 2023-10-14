from django.shortcuts import render
from products.models import Product

def index(request):
    items = {
        'products' : Product.objects.all()
    }
    return render(request , 'pages/index.html',items)


def about(request):
    return render(request , 'pages/about.html')


def coffee(request):
    return render(request , 'pages/coffee.html')
