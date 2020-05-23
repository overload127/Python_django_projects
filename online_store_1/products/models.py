from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, verbose_name='Навзание')
    is_active = models.BooleanField(default=True, verbose_name='Используется')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'


class Product(models.Model):
    name = models.CharField(
        max_length=64, blank=False, null=False, verbose_name='Название')
    description = models.TextField(
        blank=True, null=False, default='', verbose_name='Описание')
    short_description = models.CharField(
        max_length=100, blank=True, null=False, default='',
        verbose_name='Короткое описание')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена продажи')
    discount = models.IntegerField(default=0, verbose_name='Скидка')
    category = models.ForeignKey(
        ProductCategory, blank=True, null=True, default=None, 
        on_delete=models.SET_NULL, verbose_name='Категория')
    is_active = models.BooleanField(default=True, verbose_name='Используется')
    created = models.DateTimeField(
        auto_now_add=True, auto_now=False, verbose_name='Создан')
    update = models.DateTimeField(
        auto_now_add=False, auto_now=True, verbose_name='Изменен')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, blank=False, null=False, on_delete=models.CASCADE,
        verbose_name='Товар')
    image = models.ImageField(
        upload_to='products/image/', verbose_name='Изображение')
    is_main = models.BooleanField(
        default=False, verbose_name='Главная')
    is_active = models.BooleanField(
        default=True, verbose_name='Используется')
    created = models.DateTimeField(
        auto_now_add=True, auto_now=False, verbose_name='Создан')
    update = models.DateTimeField(
        auto_now_add=False, auto_now=True, verbose_name='Изменен')

    def __str__(self):
        return f'{self.product.name}'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
