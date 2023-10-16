from django.shortcuts import render,get_object_or_404
from .models import Product


def products(request):
    product =  Product.objects.all()
    if 'Searchname' in request.GET:
        name = request.GET['Searchname']
        if name:
            product = product.filter(name__icontains=name)
    
    if 'Searchdescription' in request.GET:
        desc = request.GET['Searchdescription']
        if desc:
            product = product.filter(description__icontains=desc)


    items = {
        'products':product
    }
    return render(request, 'products/products.html', items)


 
def product(request,product_id):
    item = {
        'product':get_object_or_404(Product,pk=product_id)
    }
    return render(request,'products/product.html',item)

def search(request):
    return render(request,'products/search.html')