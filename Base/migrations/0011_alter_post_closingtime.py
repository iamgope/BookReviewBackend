# Generated by Django 3.2.7 on 2021-10-28 17:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0010_auto_20211028_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ClosingTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 7, 17, 41, 45, 950524, tzinfo=utc)),
        ),
    ]
