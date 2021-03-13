from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages

from authapp.forms import FormUserLogin, FormUserRegister, FormUserProfile
from basketapp.models import Basket

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
        form = FormUserLogin()
    context = {'form': form}
    return render(request, 'authapp/login.html', context)


def register(request):
    if request.method == 'POST':
        form = FormUserRegister(data=request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Регистрация произведена!')
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = FormUserRegister()
    context = {'form': form}
    return render(request, 'authapp/register.html', context)


def profile(request):
    user = request.user
    if request.method == 'POST':
        form = FormUserProfile(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data has been changed successfully!')
            return HttpResponseRedirect(reverse('auth:profile'))
    else:
        form = FormUserProfile(instance=user)
    basket = Basket.objects.filter(user=user)
    total_quantity = 0
    total_price = 0
    for elem in basket:
        total_quantity += elem.quantity
        total_price += elem.sum()
    context = {
        'form': form,
        'baskets': basket,
        'total_quantity': total_quantity,
        'total_price': total_price,
        'title': 'GeekShop - Профиль',
    }
    return render(request, 'authapp/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
