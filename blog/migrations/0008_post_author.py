# Generated by Django 3.2.2 on 2021-06-05 15:36

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210531_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default=django.contrib.auth.models.User, max_length=100),
        ),
    ]