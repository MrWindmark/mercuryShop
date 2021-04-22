from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.core.cache import cache
from django.conf import settings

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
        # 'categories': ProductCategory.objects.all(),
        'categories': get_links_menu(),
    }
    if category_id:
        # products = Product.objects.filter(category_id=category_id).select_related('category')
        products = get_products_in_category(category_id)
    else:
        # products = Product.objects.all().select_related('category')
        products = get_all_products()
    paginator = Paginator(products, per_page=3)
    products_paginator = paginator.page(page_number)
    context.update({'products': products_paginator})
    return render(request, 'mainapp/products.html', context)


def get_links_menu():
    if settings.LOW_CACHE:
        key = 'links_menu'
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = ProductCategory.objects.all()
            cache.set(key, links_menu)
        return links_menu
    else:
        return ProductCategory.objects.all()


def get_all_products():
    if settings.LOW_CACHE:
        key = 'products'
        products = cache.get(key)
        if products is None:
            products = Product.objects.all().select_related('category')
            cache.set(key, products)
        return products
    else:
        return Product.objects.all().select_related('category')


def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product_{pk}'
        product = cache.get(key)
        if product is None:
            product = get_object_or_404(Product, pk=pk)
            cache.set(key, product)
        return product
    else:
        return get_object_or_404(Product, pk=pk)


def get_products_in_category(pk):
    if settings.LOW_CACHE:
        key = f'products_in_category_{pk}'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(category__pk=pk)
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(category__pk=pk)
