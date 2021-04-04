# Generated by Django 2.2.18 on 2021-04-04 16:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20210404_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_live_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 5, 16, 58, 45, 396939, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagline', models.CharField(blank=True, max_length=128, verbose_name='тэги')),
                ('about_myself', models.CharField(blank=True, max_length=512, verbose_name='О себе')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='Пол')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
