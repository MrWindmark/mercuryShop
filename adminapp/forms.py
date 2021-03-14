from authapp.forms import FormUserRegister, FormUserProfile
from authapp.models import User
from django import forms


class UserAdminRegistrarionForm(FormUserRegister):
    avatar = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegistrarionForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'


class UserAdminChangeForm(FormUserProfile):
    avatar = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'avatar', 'username', 'email', 'birth_date')

    def __init__(self, *args, **kwargs):
        super(FormUserProfile, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'
