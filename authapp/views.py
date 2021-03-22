from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views import View

from authapp.forms import FormUserLogin, FormUserRegister, FormUserProfile
from basketapp.models import Basket


# Create your views here.
class UserLoginView(View):
    form_class = FormUserLogin
    template_name = 'authapp/login.html'

    def get(self, request):
        context = {'form': self.form_class}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        context = {'form': form}
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse_lazy('index'))
        return render(request, self.template_name, context)


class UserRegisterVeiw(View):
    form_class = FormUserRegister
    template_name = 'authapp/register.html'

    def get(self, request):
        form = self.form_class
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            messages.info(request, 'Регистрация произведена!')
            return HttpResponseRedirect(reverse_lazy('auth:login'))
        return render(request, self.template_name, context)


class UserProfileView(View):
    form_class = FormUserProfile

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        user = request.user
        form = self.form_class(instance=user)
        context = {
            'form': form,
            'baskets': Basket.objects.filter(user=user),
            'title': 'GeekShop - Профиль',
        }
        return render(request, 'authapp/profile.html', context)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        user = request.user
        form = self.form_class(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data has been changed successfully!')
            return HttpResponseRedirect(reverse_lazy('auth:profile'))
        context = {
            'form': form,
            'baskets': Basket.objects.filter(user=user),
            'title': 'GeekShop - Профиль',
        }
        return render(request, 'authapp/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
