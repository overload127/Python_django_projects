from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(verbose_name='Емейл')
    name = models.CharField(max_length=128, verbose_name='Имя подписчика')

    def __str__(self):
        return f'Пользователь {self.email:-<50} {self.name}'

    class Meta:
        verbose_name = 'My Subscriber'
        verbose_name_plural = 'A lot of subscribers'
