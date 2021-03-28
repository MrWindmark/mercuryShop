from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views import View

from authapp.forms import FormUserLogin, FormUserRegister, FormUserProfile
from authapp.models import User


# Create your views here.
from django.conf import settings


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


class UserVerifyView(View):
    form_class = FormUserRegister
    template_name = 'authapp/login.html'

    def get(self, request, username, activation_key):
        try:
            user = User.objects.get(username=username)
            if user.activation_key == activation_key and not user.activation_key_valid_check():
                user.is_active = True
                user.save()
                messages.info(request, 'Активация профиля завершена!')
                return HttpResponseRedirect(reverse_lazy('authapp:login'))
            else:
                return HttpResponseRedirect(reverse_lazy('index'))
        except Exception as e:
            print(f'error activation user : {e.args}')
            return HttpResponseRedirect(reverse_lazy('index'))


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
            user = form.save()
            self.send_email_for_verify(request, user)
            messages.info(request, 'Регистрация произведена! Активация профиля через указанный e-mail')
            return HttpResponseRedirect(reverse_lazy('auth:login'))
        return render(request, self.template_name, context)

    def send_email_for_verify(self, request, user):
        verify_link = reverse('authapp:verify', args=[user.username, user.activation_key])
        title = f'Активация профиля GeekShop'
        email_text = f'Для активации пользователя перейдите по ссылке: \n{request.META["HTTP_HOST"]}' \
                     f'{verify_link}' \
                     f'\n\nЕсли вы не регистрировались на сайте, проигнорируйте данное сообщение'
        return send_mail(title, email_text, settings.EMAIL_HOST_USER, [user.email, ])


class UserProfileView(View):
    form_class = FormUserProfile

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        user = request.user
        form = self.form_class(instance=user)
        context = {
            'form': form,
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
            'title': 'GeekShop - Профиль',
        }
        return render(request, 'authapp/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
