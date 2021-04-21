from django.db import models
from django.utils.functional import cached_property

from authapp.models import User
from mainapp.models import Product


# Changes in basket don't mean that order created
# class BasketQuerySet(models.QuerySet):
#
#    def delete(self, *args, **kwargs):
#        for object in self:
#            object.product.quantity -= object.quantity
#            object.product.save()
#        super(BasketQuerySet, self).delete(*args, **kwargs)


# Create your models here.
class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    # objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    # Changes in basket don't mean that order created
    # def save(self, *args, **kwargs):
    #     if self.pk:
    #         self.product.quantity -= self.quantity - \
    #                                  self.__class__.get_item(self.pk).quantity
    #     else:
    #         self.product.quantity -= self.quantity
    #     self.product.save()
    #     super(self.__class__, self).save(*args, **kwargs)

    @cached_property
    def get_cached_items(self):
        return self.user.basket_set.select_related()

    def sum(self):
        return self.quantity * self.product.price

    def total_quantity(self):
        _items = self.get_cached_items
        # return sum(basket.quantity for basket in Basket.objects.filter(user=self.user))
        return sum(list(map(lambda obj: obj.quantity, _items)))

    def total_price(self):
        _items = self.get_cached_items
        # return sum(basket.sum() for basket in Basket.objects.filter(user=self.user))
        return sum(list(map(lambda obj: obj.sum(), _items)))

