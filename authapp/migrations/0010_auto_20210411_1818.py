# Generated by Django 2.2.18 on 2021-04-11 15:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0009_auto_20210407_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_live_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 12, 15, 18, 55, 961063, tzinfo=utc)),
        ),
    ]