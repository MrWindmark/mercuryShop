from django.urls import path, re_path
from authapp.views import logout
from authapp.views import UserLoginView, UserRegisterView, UserProfileView, UserVerifyView
from ordersapp.views import OrderList, OrderCreate, OrderRead, OrderUpdate, OrderDelete, order_forming_complete

app_name = 'ordersapp'

urlpatterns = [
   path('orders-list/', OrderList.as_view(), name='orders_list'),
   path('forming/complete/<pk>', order_forming_complete, name='order_forming_complete'),
   path('create/', OrderCreate.as_view(), name='order_create'),
   path('read/<pk>', OrderRead.as_view(), name='order_read'),
   path('update/<pk>', OrderUpdate.as_view(), name='order_update'),
   path('delete/<pk>', OrderDelete.as_view(), name='order_delete'),
]
