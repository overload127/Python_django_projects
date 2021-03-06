# Generated by Django 3.0.5 on 2020-05-23 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200523_0903'),
        ('orders', '0004_auto_20200522_1729'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinorder',
            options={'verbose_name': 'Товар в корзине', 'verbose_name_plural': 'Товары в корзине'},
        ),
        migrations.CreateModel(
            name='ProductInBasket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1, verbose_name='Количество')),
                ('price_per_item', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена продажи')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма позиции')),
                ('is_active', models.BooleanField(default=True, verbose_name='Используется')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('order', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order', verbose_name='Заказ')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Товар в заказе',
                'verbose_name_plural': 'Товары в заказе',
            },
        ),
    ]
