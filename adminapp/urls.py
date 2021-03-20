from django.urls import path
from adminapp.views import (index, admin_product_read, admin_product_create,
                            admin_product_update, admin_product_delete)
from adminapp.views import UserListView, UserCreateView, UserUpdateView, UserDeleteView

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='users_read'),
    path('create-user/', UserCreateView.as_view(), name='create-user'),
    path('update-user/<int:pk>/', UserUpdateView.as_view(), name='update_user'),
    path('delete-user/<int:pk>', UserDeleteView.as_view(), name='delete_user'),
    path('list-product/', admin_product_read, name='read-product'),
    path('create-product/', admin_product_create, name='create-product'),
    path('update-product/<int:product_id>/', admin_product_update, name='update_product'),
    path('delete-product/<int:product_id>', admin_product_delete, name='delete_product'),
]
