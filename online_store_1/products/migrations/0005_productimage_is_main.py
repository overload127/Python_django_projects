# Generated by Django 3.0.5 on 2020-05-22 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Главная'),
        ),
    ]