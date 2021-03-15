from django.urls import path
from basketapp.views import basket_add, basket_remove

app_name = 'basketapp'

urlpatterns = [
    path('basket-add/<prod_id>', basket_add, name='basket_add'),
    path('basket-del/<basket_id>', basket_remove, name='basket_remove'),
]