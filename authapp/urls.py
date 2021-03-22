from django.urls import path
from authapp.views import logout
from authapp.views import UserLoginView, UserRegisterVeiw, UserProfileView

app_name = 'authapp'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterVeiw.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('logout/', logout, name='logout'),
]
