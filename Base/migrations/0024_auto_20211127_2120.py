# Generated by Django 3.2.7 on 2021-11-27 15:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Base', '0023_finalresponse_associatedpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalresponse',
            name='isLiked',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='finalresponse',
            unique_together={('AssociatedPost', 'User')},
        ),
    ]
