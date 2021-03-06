# Generated by Django 3.2.7 on 2021-11-26 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Base', '0019_post_postdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Response', models.TextField()),
                ('username', models.CharField(max_length=100)),
                ('isLiked', models.BooleanField(default=False)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='response',
            name='User',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='response',
            name='type',
            field=models.CharField(default='subjective', max_length=100),
        ),
        migrations.AddField(
            model_name='response',
            name='username',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='PostData',
        ),
    ]
