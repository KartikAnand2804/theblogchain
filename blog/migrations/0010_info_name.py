# Generated by Django 3.2.2 on 2021-06-05 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='name',
            field=models.CharField(default='SharingInc.', max_length=100),
        ),
    ]
