from django.db import models

from authapp.models import User
from mainapp.models import Product


# Create your models here.
class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    def total_quantity(self):
        return sum(basket.quantity for basket in Basket.objects.filter(user=self.user))

    def total_price(self):
        return sum(basket.sum() for basket in Basket.objects.filter(user=self.user))
