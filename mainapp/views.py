from django.core.paginator import Paginator
from django.shortcuts import render

from mainapp.models import Product, ProductCategory


# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, category_id=None, page_number=1):
    context = {
        'title': 'GeekShop - Каталог',
        'categories': ProductCategory.objects.all(),
    }
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, per_page=3)
    products_paginator = paginator.page(page_number)
    context.update({'products': products_paginator})
    return render(request, 'mainapp/products.html', context)
