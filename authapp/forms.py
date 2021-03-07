from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from authapp.models import User


class FormUserLogin(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class FormUserRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
