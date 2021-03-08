from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages

from authapp.forms import FormUserLogin, FormUserRegister


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = FormUserLogin(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print('Error')
    else:
        form = FormUserLogin()
        context = {'form': form}
        return render(request, 'authapp/login.html', context)


def register(request):
    if request.method == 'POST':
        form = FormUserRegister(data=request.POST)
        if form.is_valid():
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password2']
            pass
    else:
        form = FormUserRegister()
        context = {'form': form}
        return render(request, 'authapp/register.html', context)


def profile(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        return render(request, 'authapp/profile.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:index'))
