from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.models import User
from adminapp.forms import UserAdminRegistrarionForm

# Create your views here.


def index(request):
    return render(request, 'adminapp/admin.html')


def admin_user_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrarionForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:users_read'))
    else:
        form = UserAdminRegistrarionForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-users-create.html', context)


def admin_user_read(request):
    context = {'users': User.objects.all()}
    return render(request, 'adminapp/admin-users-read.html', context)


def admin_user_update(request):
    return render(request, 'adminapp/admin-users-update-delete.html')


def admin_user_delete(request):
    return render(request, 'adminapp/admin-users-update-delete.html')
