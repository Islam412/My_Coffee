from django.shortcuts import render,get_object_or_404
from .models import Product


def products(request):
    product =  Product.objects.all()
    cs = request.GET.get('cs', 'off')
    
    if 'Searchname' in request.GET:
        name = request.GET['Searchname']
        if name:
            if cs == 'on':
                product = product.filter(name__contains=name)
            else:
                product = product.filter(name__icontains=name)
    
    if 'Searchdescription' in request.GET:
        desc = request.GET['Searchdescription']
        if desc:
            if cs == 'on':
                product = product.filter(description__contains=desc)
            else:
                product = product.filter(description__icontains=desc)

    
    if 'Searchpricefrom' in request.GET and 'Searchpriceto' in request.GET:
        price_from = request.GET['Searchpricefrom']
        price_to = request.GET['Searchpriceto']
        if price_from.isdigit() and price_to.isdigit():
            product = product.filter(price__gte=price_from,price__lte=price_to)  # get----> >= , lte----> <=
    
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