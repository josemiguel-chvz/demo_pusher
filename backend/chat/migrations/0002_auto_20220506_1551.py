# Generated by Django 3.0.5 on 2022-05-06 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messagemodel',
            name='user',
        ),
        migrations.AddField(
            model_name='messagemodel',
            name='username',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
