# Generated by Django 2.2.18 on 2021-04-07 19:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_auto_20210404_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_live_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 8, 19, 8, 25, 530395, tzinfo=utc)),
        ),
    ]