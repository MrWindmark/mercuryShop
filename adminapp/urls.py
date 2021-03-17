from django.urls import path
from adminapp.views import (index, admin_user_read, admin_user_create, admin_user_update, admin_user_delete,
                            admin_product_read, admin_product_create, )

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_user_read, name='users_read'),
    path('create-user/', admin_user_create, name='create-user'),
    path('update-user/<int:user_id>/', admin_user_update, name='update_user'),
    path('delete-user/<int:user_id>', admin_user_delete, name='delete_user'),
    path('list-product/', admin_product_read, name='read-product'),
    path('create-product/', admin_product_create, name='create-product'),
    # path('update-product/<int:user_id>/', admin_product_update, name='update_product'),
    # path('delete-product/<int:user_id>', admin_product_delete, name='delete_product'),
]
