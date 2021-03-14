from django.urls import path
from adminapp.views import index, admin_user_read, admin_user_create, admin_user_update, admin_user_delete

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_user_read, name='users_read'),
    path('create-user/', admin_user_create, name='create-user'),
    path('update-user/<int:user_id>/', admin_user_update, name='update_user'),
    path('delete-user/<int:user_id>', admin_user_delete, name='delete_user'),
]
