from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse
from mainapp.models import Product
from basketapp.models import Basket


# Create your views here.
@login_required
def basket_add(request, prod_id=None):
    curr_product = Product.objects.get(id=prod_id)
    curr_basket = Basket.objects.filter(user=request.user, product=curr_product)

    if not curr_basket.exists():
        basket = Basket(user=request.user, product=curr_product)
        basket.quantity = 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = curr_basket.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, basket_id=None):
    curr_basket = Basket.objects.get(user=request.user, id=basket_id)
    curr_basket.delete()
    return HttpResponseRedirect(reverse('auth:profile'))


@login_required
def basket_edit(request, basket_id, quantity):
    if request.is_ajax():
        basket = Basket.objects.get(id=basket_id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
        result = render_to_string('basketapp/basket.html')
        return JsonResponse({'result': result})
