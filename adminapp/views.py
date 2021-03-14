from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'adminapp/admin.html')


def admin_user_create(request):
    return render(request, 'adminapp/admin-users-create.html')


def admin_user_read(request):
    return render(request, 'adminapp/admin-users-read.html')


def admin_user_update(request):
    return render(request, 'adminapp/admin-users-update-delete.html')


def admin_user_delete(request):
    return render(request, 'adminapp/admin-users-update-delete.html')
