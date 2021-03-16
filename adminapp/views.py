from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.models import User
from adminapp.forms import UserAdminRegistrationForm, UserAdminChangeForm


# Create your views here.
from mainapp.models import Product


def index(request):
    return render(request, 'adminapp/admin.html')


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


def admin_user_read(request):
    context = {'users': User.objects.all()}
    return render(request, 'adminapp/admin-users-read.html', context)


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


def admin_user_delete(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active =False
    user.save()
    return HttpResponseRedirect(reverse('staff_admin:users_read'))


# def admin_user_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:users_read'))
#     else:
#         form = UserAdminRegistrationForm()
#     context = {'form': form}
#     return render(request, 'adminapp/admin-users-create.html', context)
#
#
# def admin_product_read(request):
#     context = {'users': Product.objects.all()}
#     return render(request, 'adminapp/admin-product-read.html', context)
#
#
# def admin_product_update(request, user_id):
#     user = Product.objects.get(id=user_id)
#     # if request.method == 'POST':
#     #     form = UserAdminChangeForm(data=request.POST, files=request.FILES, instance=user)
#     #     if form.is_valid():
#     #         form.save()
#     #         return HttpResponseRedirect(reverse('staff_admin:users_read'))
#     # else:
#     #     form = UserAdminChangeForm(instance=user)
#     # context = {
#     #     'form': form,
#     #     'user': user,
#     # }
#     return render(request, 'adminapp/admin-users-update-delete.html') #, context)
#
#
# def admin_product_delete(request, product_id):
#     product = Product.objects.get(id=product_id)
#     product.delete()
#     return HttpResponseRedirect(reverse('staff_admin:'))