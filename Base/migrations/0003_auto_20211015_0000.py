# Generated by Django 3.2.7 on 2021-10-14 18:30

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0002_auto_20211013_0121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option1', models.TextField(null=True)),
                ('option2', models.TextField(null=True)),
                ('option3', models.TextField(null=True)),
                ('option4', models.TextField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='objectiveresponse',
            name='question',
        ),
        migrations.RemoveField(
            model_name='subjectivequestion',
            name='AssociatedPost',
        ),
        migrations.RenameField(
            model_name='subscribedposts',
            old_name='user',
            new_name='User',
        ),
        migrations.AlterField(
            model_name='post',
            name='ClosingTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 24, 18, 29, 45, 842137, tzinfo=utc)),
        ),
        migrations.RenameModel(
            old_name='SubjectiveResponse',
            new_name='Response',
        ),
        migrations.DeleteModel(
            name='ObjectiveQuestion',
        ),
        migrations.DeleteModel(
            name='ObjectiveResponse',
        ),
        migrations.DeleteModel(
            name='SubjectiveQuestion',
        ),
        migrations.AddField(
            model_name='question',
            name='AssociatedPost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.post'),
        ),
        migrations.AlterField(
            model_name='response',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.question'),
        ),
    ]
