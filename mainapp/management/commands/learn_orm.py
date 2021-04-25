from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from django.db import connection
from django.db.models import Q
from mainapp.views import db_profile_by_type

class Command(BaseCommand):
   def handle(self, *args, **options):
       test_products = Product.objects.filter(
           Q(category__name='Одежда') |
           Q(category__name='Новинки')
       )
       test_products2 = Product.objects.filter(
           Q(category__name__icontains='дежда') |
           Q(category__name='Новинки')
       )
       test_products3 = Product.objects.filter(
           Q(category__name__iregex=r'одежда') |
           Q(category__name='Новинки')
       )


       print(len(test_products))
       print(len(test_products2))
       print(len(test_products3))
       # print(test_products)

       db_profile_by_type('learn db', '', connection.queries)