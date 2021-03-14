from django.urls import path
from adminapp.views import index, admin_user_read, admin_user_create, admin_user_update, admin_user_delete

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_user_read, name='users_read'),
    # path('users/', admin_user_read, name='users_read'),
    # path('', index, name='index'),
]
