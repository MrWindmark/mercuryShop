from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from authapp.models import User
from adminapp.forms import UserAdminRegistrationForm, UserAdminChangeForm, AdminProductCreationForm
from mainapp.models import Product, ProductCategory


@user_passes_test(lambda user: user.is_superuser, login_url='/')
def index(request):
    return render(request, 'adminapp/admin.html')


@user_passes_test(lambda user: user.is_superuser, login_url='/')
def admin_user_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:users_read'))
    else:
        form = UserAdminRegistrationForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-users-create.html', context)


@user_passes_test(lambda user: user.is_superuser, login_url='/')
def admin_user_read(request):
    context = {'users': User.objects.all()}
    return render(request, 'adminapp/admin-users-read.html', context)


@user_passes_test(lambda user: user.is_superuser, login_url='/')
def admin_user_update(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserAdminChangeForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('staff_admin:users_read'))
    else:
        form = UserAdminChangeForm(instance=user)
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'adminapp/admin-users-update-delete.html', context)


@user_passes_test(lambda user: user.is_superuser, login_url='/')
def admin_user_delete(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return HttpResponseRedirect(reverse('staff_admin:users_read'))


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
