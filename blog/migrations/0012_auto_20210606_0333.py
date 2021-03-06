# Generated by Django 3.2.2 on 2021-06-05 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20210606_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='email',
            field=models.EmailField(default='sharinginc.work@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='info',
            name='phone',
            field=models.CharField(default='9999999999', max_length=10),
        ),
        migrations.AddField(
            model_name='info',
            name='website',
            field=models.CharField(default='https://sharinginc.github.io/SharingInc/', max_length=200),
        ),
    ]
