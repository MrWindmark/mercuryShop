# Generated by Django 2.2.18 on 2021-04-04 19:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20210404_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveSmallIntegerField(default=18, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='user',
            name='activation_key_live_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 5, 19, 44, 7, 962707, tzinfo=utc)),
        ),
    ]
