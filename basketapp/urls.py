from django.urls import path
from basketapp.views import basket_add, basket_rem

app_name = 'basketapp'

urlpatterns = [
    path('basket-add/<prod_id>', basket_add, name='basket_add'),
    path('basket-del/<basket_id>', basket_rem, name='basket_rem'),
]