# Generated by Django 3.0.5 on 2020-05-23 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200523_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinbasket',
            name='session_key',
            field=models.CharField(default='123', max_length=128),
            preserve_default=False,
        ),
    ]
