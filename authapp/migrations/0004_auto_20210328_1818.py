# Generated by Django 2.2.18 on 2021-03-28 15:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20210310_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='activation_key',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='user',
            name='activation_key_live_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 29, 15, 18, 56, 602106, tzinfo=utc)),
        ),
    ]
