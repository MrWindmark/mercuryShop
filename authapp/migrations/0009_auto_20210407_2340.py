# Generated by Django 2.2.18 on 2021-04-07 20:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_auto_20210407_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_live_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 8, 20, 40, 42, 729087, tzinfo=utc)),
        ),
    ]