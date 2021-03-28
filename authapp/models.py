from datetime import timedelta
from django.utils.timezone import now

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatar', blank=True)
    birth_date = models.DateField(blank=True, null=True)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_live_time = models.DateTimeField(default=(now() + timedelta(hours=24)))

    def activation_key_valid_check(self):
        return not(now() <= self.activation_key_live_time)