from django.urls import path
from django.views.decorators.cache import cache_page

from mainapp.views import products, item, products_ajax

app_name = 'mainapp'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:category_id>/', products, name='category'),
    path('item/<int:id>/', item, name='item'),
    path('page/<int:page_number>/', products, name='page'),
    path('category/<pk>/ajax/', cache_page(3600)(products_ajax)),
    path('category/<pk>/page/<page>/ajax/', cache_page(3600)(products_ajax))
]
