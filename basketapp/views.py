from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from mainapp.models import Product
from basketapp.models import Basket


# Create your views here.
def basket_add(request, prod_id=None):
    curr_product = Product.objects.get(id=prod_id)
    curr_basket = Basket.objects.filter(user=request.user, product=curr_product)

    if not curr_basket.exists():
        basket = Basket(user=request.user, product=curr_product)
        basket.quantity = 1
        basket.save()
        return HttpResponseRedirect(reverse('auth:profile'))
    else:
        basket = curr_basket.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(reverse('auth:profile'))


def basket_remove(request, basket_id=None):
    curr_basket = Basket.objects.get(user=request.user, id=basket_id)
    curr_basket.delete()
    return HttpResponseRedirect(reverse('auth:profile'))
