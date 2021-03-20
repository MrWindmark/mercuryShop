from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from authapp.models import User
from adminapp.forms import UserAdminRegistrationForm, UserAdminChangeForm, AdminProductCreationForm
from mainapp.models import Product, ProductCategory


@user_passes_test(lambda user: user.is_superuser, login_url='/')
def index(request):
    return render(request, 'adminapp/admin.html')


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
    success_url = reverse_lazy('adminapp:users_read')

    @method_decorator(user_passes_test(lambda user: user.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(CreateView, self).dispatch(request, *args, **kwargs)


class UserUpdateView(UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminChangeForm
    success_url = reverse_lazy('adminapp:users_read')

    @method_decorator(user_passes_test(lambda user: user.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(UpdateView, self).dispatch(request, *args, **kwargs)


class UserDeleteView(DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('adminapp:users_read')

    @method_decorator(user_passes_test(lambda user: user.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(DeleteView, self).dispatch(request, *args, **kwargs)


@user_passes_test(lambda user: user.is_superuser, login_url='/')
def admin_user_disable(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('staff_admin:users_read'))


@user_passes_test(lambda user: user.is_superuser, login_url='/')
def admin_product_read(request):
    context = {'products': Product.objects.all(), 'categories': ProductCategory.objects.all(),}
    return render(request, 'adminapp/admin-products-read.html', context)


@user_passes_test(lambda user: user.is_superuser, login_url='/')
def admin_product_create(request):
    if request.method == 'POST':
        form = AdminProductCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('staff_admin:read-product'))
    else:
        form = AdminProductCreationForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-products-create.html', context)


@user_passes_test(lambda user: user.is_superuser, login_url='/')
def admin_product_update(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = AdminProductCreationForm(data=request.POST, files=request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('staff_admin:read-product'))
    else:
        form = AdminProductCreationForm(instance=product)
    context = {
        'form': form,
        'product': product
    }
    return render(request, 'adminapp/admin-products-edit.html', context)


@user_passes_test(lambda user: user.is_superuser, login_url='/')
def admin_product_delete(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return HttpResponseRedirect(reverse('staff_admin:read-product'))
