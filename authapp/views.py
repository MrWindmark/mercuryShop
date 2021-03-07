from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, 'authapp/login.html')


def register(request):
    return render(request, 'authapp/register.html')


def profile(request):
    return render(request, 'authapp/profile.html')
