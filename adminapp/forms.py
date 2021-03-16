from authapp.forms import FormUserRegister, FormUserProfile
from authapp.models import User
from django import forms


class UserAdminRegistrationForm(FormUserRegister):
    avatar = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'is_active', 'is_staff')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'


class UserAdminChangeForm(FormUserProfile):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'is_active', 'is_staff', 'is_superuser')

    def __init__(self, *args, **kwargs):
        super(UserAdminChangeForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False
        for field_name, field in self.fields.items():
            if field_name == 'is_active' or field_name == 'is_staff' or field_name == 'is_superuser':
                field.widget.attrs['class'] = 'py-4'
