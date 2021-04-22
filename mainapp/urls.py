from django.urls import path
from mainapp.views import products, item

app_name = 'mainapp'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:category_id>/', products, name='category'),
    path('item/<int:id>/', item, name='item'),
    path('page/<int:page_number>/', products, name='page'),
]