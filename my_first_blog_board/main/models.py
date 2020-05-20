from django.contrib.auth.models import AbstractUser
from django.db import models


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(
        default=False, db_index=True, verbose_name='Прошел активацию?')
    send_message = models.BooleanField(
        default=True, verbose_name='Слать оповещения о новых коментариях?')

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class LesonTube(models.Model):
    title = models.CharField(
        max_length=250, db_index=True, verbose_name='Название видео-урока')
    path_file = models.FileField(max_length=100, verbose_name='Видео-урок')

    def __str__(self):
        return ''

    class Meta:
        pass
