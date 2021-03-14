from django.urls import path
from basketapp.views import basket_add, basket_remove, basket_edit

app_name = 'basketapp'

urlpatterns = [
    path('basket-add/<prod_id>', basket_add, name='basket_add'),
    path('basket-del/<basket_id>', basket_remove, name='basket_remove'),
    path('edit/<int:basket_id>/<int:quantity>/', basket_edit, name='basket_edit'),
]