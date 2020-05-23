from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from products.models import Product


class Status(models.Model):
    name = models.CharField(
        max_length=24, blank=False, null=False,
        verbose_name='Название')
    is_active = models.BooleanField(default=True, verbose_name='Используется')
    created = models.DateTimeField(
        auto_now_add=True, auto_now=False,
        verbose_name='Создан')
    update = models.DateTimeField(
        auto_now_add=False, auto_now=True,
        verbose_name='Изменен')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'


class Order(models.Model):
    customer_name = models.CharField(
        max_length=64, blank=True, null=True, default=None,
        verbose_name='Покупатель')
    customer_email = models.EmailField(
        blank=True, null=True, default=None,
        verbose_name='Емейл')
    customer_phone = models.CharField(
        max_length=48, blank=True, null=True, default=None,
        verbose_name='Телефон')
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Сумма всего заказа')
    customer_adress = models.CharField(
        max_length=250, blank=False, null=False,
        verbose_name='Адрес')
    comments = models.TextField(
        blank=True, null=True, default=None,
        verbose_name='Комментарий')
    status = models.ForeignKey(
        Status, null=True, default=None, on_delete=models.SET_NULL,
        verbose_name='Статус')
    created = models.DateTimeField(
        auto_now_add=True, auto_now=False,
        verbose_name='Создан')
    update = models.DateTimeField(
        auto_now_add=False, auto_now=True,
        verbose_name='Изменен')

    def __str__(self):
        if self.status:
            return f'Заказ {self.id} {self.status.name}'
        else:
            return f'Заказ {self.id} без статуса'

    def save(self, *args, **kwargs):
        product_in_order = ProductInOrder.objects.filter(order=self, is_active=True)
        order_total_price = 0
        for product in product_in_order:
            order_total_price += product.total_price
        self.total_price = order_total_price
        super(Order, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductInOrder(models.Model):
    order = models.ForeignKey(
        Order, blank=True, null=True, default=None, on_delete=models.CASCADE,
        verbose_name='Заказ')
    product = models.ForeignKey(
        Product, blank=True, null=True, default=None, on_delete=models.CASCADE,
        verbose_name='Продукт')
    number = models.IntegerField(default=1, verbose_name='Количество')
    price_per_item = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена продажи')
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Сумма позиции')
    is_active = models.BooleanField(default=True, verbose_name='Используется')
    created = models.DateTimeField(
        auto_now_add=True, auto_now=False,
        verbose_name='Создан')
    update = models.DateTimeField(
        auto_now_add=False, auto_now=True,
        verbose_name='Изменен')

    def save(self, *args, **kwargs):
        price_item = self.product.price
        self.price_per_item = price_item
        self.total_price = price_item * self.number
        super(ProductInOrder, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name}'

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'


@receiver(post_save, sender=ProductInOrder)
def product_in_order_save(sender, instance, *args, **kwargs):
    instance.order.save()


class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128)
    order = models.ForeignKey(
        Order, blank=True, null=True, default=None, on_delete=models.CASCADE,
        verbose_name='Заказ')
    product = models.ForeignKey(
        Product, blank=True, null=True, default=None, on_delete=models.CASCADE,
        verbose_name='Продукт')
    number = models.IntegerField(default=1, verbose_name='Количество')
    price_per_item = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена продажи',
        blank=True, null=True, default=None)
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Сумма позиции',
        blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True, verbose_name='Используется')
    created = models.DateTimeField(
        auto_now_add=True, auto_now=False,
        verbose_name='Создан')
    update = models.DateTimeField(
        auto_now_add=False, auto_now=True,
        verbose_name='Изменен')

    def __str__(self):
        return f'{self.product.name}'

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'
