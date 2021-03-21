from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from authapp.models import User
from adminapp.forms import UserAdminRegistrationForm, UserAdminChangeForm, AdminProductCreationForm
from adminapp.forms import ProductCategoryAdminReadForm
from mainapp.models import Product, ProductCategory


@user_passes_test(lambda user: user.is_superuser, login_url='/')
def index(request):
    return render(request, 'adminapp/admin.html')


@user_passes_test(lambda user: user.is_superuser, login_url='/')
def admin_user_disable(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('staff_admin:users_read'))


class UserListView(ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'

    @method_decorator(user_passes_test(lambda user: user.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegistrationForm
    success_url = reverse_lazy('adminapp:users-read')

    @method_decorator(user_passes_test(lambda user: user.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


class UserUpdateView(UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminChangeForm
    success_url = reverse_lazy('adminapp:users-read')

    @method_decorator(user_passes_test(lambda user: user.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


class UserDeleteView(DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('adminapp:users-read')

    @method_decorator(user_passes_test(lambda user: user.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)


class ProductListView(ListView):
    model = Product
    template_name = 'adminapp/admin-products-read.html'

    @method_decorator(user_passes_test(lambda user: user.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductListView, self).dispatch(request, *args, **kwargs)


class ProductCreateView(CreateView):
    model = Product
    template_name = 'adminapp/admin-products-create.html'
    form_class = AdminProductCreationForm
    success_url = reverse_lazy('staff_admin:read-product')

    @method_decorator(user_passes_test(lambda user: user.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCreateView, self).dispatch(request, *args, **kwargs)


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'adminapp/admin-products-edit.html'
    form_class = AdminProductCreationForm
    success_url = reverse_lazy('staff_admin:read-product')

    @method_decorator(user_passes_test(lambda user: user.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductUpdateView, self).dispatch(request, *args, **kwargs)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/admin-products-edit.html'
    success_url = reverse_lazy('adminapp:read-product')

    @method_decorator(user_passes_test(lambda user: user.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductDeleteView, self).dispatch(request, *args, **kwargs)


class ProductCategoryListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/admin-products-category-read.html'

    @method_decorator(user_passes_test(lambda user: user.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCategoryListView, self).dispatch(request, *args, **kwargs)


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/admin-products-category-create.html'
    form_class = ProductCategoryAdminReadForm
    success_url = reverse_lazy('staff_admin:read-product-category')

    @method_decorator(user_passes_test(lambda user: user.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCategoryCreateView, self).dispatch(request, *args, **kwargs)


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/admin-products-category-edit.html'
    form_class = ProductCategoryAdminReadForm
    success_url = reverse_lazy('staff_admin:read-product-category')

    @method_decorator(user_passes_test(lambda user: user.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCategoryUpdateView, self).dispatch(request, *args, **kwargs)


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/admin-products-category-edit.html'
    success_url = reverse_lazy('adminapp:read-product-category')

    @method_decorator(user_passes_test(lambda user: user.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCategoryDeleteView, self).dispatch(request, *args, **kwargs)
