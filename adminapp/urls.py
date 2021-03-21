from django.urls import path
from adminapp.views import index
from adminapp.views import UserListView, UserCreateView, UserUpdateView, UserDeleteView
from adminapp.views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView
from adminapp.views import (ProductCategoryListView, ProductCategoryCreateView, ProductCategoryUpdateView,
                            ProductCategoryDeleteView)

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='users-read'),
    path('create-user/', UserCreateView.as_view(), name='create-user'),
    path('update-user/<int:pk>/', UserUpdateView.as_view(), name='update-user'),
    path('delete-user/<int:pk>/', UserDeleteView.as_view(), name='delete-user'),

    path('list-product/', ProductListView.as_view(), name='read-product'),
    path('create-product/', ProductCreateView.as_view(), name='create-product'),
    path('update-product/<int:pk>/', ProductUpdateView.as_view(), name='update-product'),
    path('delete-product/<int:pk>/', ProductDeleteView.as_view(), name='delete-product'),

    path('list-product-category/', ProductCategoryListView.as_view(), name='read-product-category'),
    path('create-product-category/', ProductCategoryCreateView.as_view(), name='create-product-category'),
    path('update-product-category/<int:pk>/', ProductCategoryUpdateView.as_view(), name='update-product-category'),
    path('delete-product-category/<int:pk>/', ProductCategoryDeleteView.as_view(), name='delete-product-category'),
]
