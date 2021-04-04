from datetime import timedelta

from django.utils.datetime_safe import date
from django.utils.timezone import now

from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatar', blank=True)
    birth_date = models.DateField(blank=True, default='1970-01-01')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', default=18)


    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_live_time = models.DateTimeField(default=(now() + timedelta(hours=24)))

    def activation_key_valid_check(self):
        return not (now() <= self.activation_key_live_time)


class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female")
    )

    user = models.OneToOneField(
        User,
        unique=True,
        null=False,
        db_index=True,
        on_delete=models.CASCADE
    )

    tagline = models.CharField(
        verbose_name='тэги',
        max_length=128,
        blank=True
    )

    about_myself = models.CharField(
        verbose_name='О себе',
        max_length=512,
        blank=True
    )

    gender = models.CharField(
        verbose_name='Пол',
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True
    )

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, *args, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, *args, **kwargs):
        instance.userprofile.save()