from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.core.cache import cache
from django.conf import settings
from django.views.decorators.cache import cache_page

from django.template.loader import render_to_string
from django.http import JsonResponse

from mainapp.models import Product, ProductCategory


# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


@cache_page(3600)
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


def item(request, id):
    context = {
        'title': 'GeekShop - Каталог',
        'categories': get_links_menu(),
        'item': get_product(id),
    }
    return render(request, 'mainapp/item.html', context)


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

def get_category(pk):
    if settings.LOW_CACHE:
        key = f'category_{pk}'
        category = cache.get(key)
        if category is None:
            category = get_object_or_404(ProductCategory, pk=pk)
            cache.set(key, category)
        return category
    else:
        return get_object_or_404(ProductCategory, pk=pk)


def products_ajax(request, pk=None, page=1):
    if request.is_ajax():
        links_menu = get_links_menu()

        if pk:
            if pk == '0':
                category = {
                    'pk': 0,
                    'name': 'все'
                }
                products = get_all_products()
            else:
                category = get_category(pk)
                products = get_products_in_category(pk)

            paginator = Paginator(products, 2)
            try:
                products_paginator = paginator.page(page)
            except PageNotAnInteger:
                products_paginator = paginator.page(1)
            except EmptyPage:
                products_paginator = paginator.page(paginator.num_pages)

            content = {
                'links_menu': links_menu,
                'category': category,
                'products': products_paginator,
            }

            result = render_to_string(
                'mainapp/products_list_inc.html',
                context=content,
                request=request)

            return JsonResponse({'result': result})
