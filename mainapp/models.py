from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Product Categories'


class SaleSpecial(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    active = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=128, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    img_linked = models.ImageField(upload_to='products_images', blank=True)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, null=True, on_delete=models.SET_NULL)
    sale_action = models.ForeignKey(SaleSpecial, null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        return f'{self.name} | {self.category}'
