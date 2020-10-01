from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})

def product_detail(request, product_pk):
    product = get_object_or_404(Product,pk = product_pk)
    product.views += 1
    product.save()
    return render(request, 'product/product_detail.html', {'product': product})
