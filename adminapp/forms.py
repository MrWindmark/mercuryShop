from authapp.forms import FormUserRegister, FormUserProfile
from authapp.models import User
from mainapp.models import Product, ProductCategory, SaleSpecial
from django import forms
from django.db import models


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


class AdminProductCreationForm(forms.ModelForm):
    img_linked = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = Product
        fields = ('name', 'description', 'short_description',
                  'price', 'img_linked', 'quantity', 'category', 'sale_action')

    def __init__(self, *args, **kwargs):
        super(AdminProductCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-2'
        self.fields['img_linked'].widget.attrs['class'] = 'custom-file-input'


class AdminProductReadForm(forms.ModelForm):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=128, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    img_linked = models.ImageField(upload_to='products_images', blank=True)
    quantity = models.PositiveIntegerField(default=0)
    category = forms.ModelChoiceField(ProductCategory.objects.all(), empty_label=None)
    sale_action = forms.ModelChoiceField(SaleSpecial.objects.all(), empty_label=None)

    class Meta:
        model = Product
        fields = ('name', 'description', 'short_description',
                  'price', 'img_linked', 'quantity', 'category', 'sale_action')

    def __init__(self, *args, **kwargs):
        super(AdminProductReadForm, self).__init__(*args, **kwargs)
        self.fields['img_linked'].widget.attrs['class'] = 'custom-file-input'


class ProductCategoryAdminReadForm(forms.ModelForm):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        model = ProductCategory
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super(ProductCategoryAdminReadForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-2'
