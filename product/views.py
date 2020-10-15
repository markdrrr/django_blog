from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})


def product_detail(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    product.views += 1
    product.save()
    images = Image.objects.filter(product=product)
    return render(request, 'product/product_detail.html', {'product': product, 'images': images})


def product_in_basket(request):
    products = ProductInBasket.objects.filter(bascket=request.user.id)
    basket = get_object_or_404(Basket, user=request.user)
    return render(request, 'product/product_in_basket.html', {'products': products, 'tp': basket.total_price})
