from django.contrib.auth.models import AbstractUser
from django.db import models


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(
        default=False, db_index=True, verbose_name='Прошел активацию?')
    send_message = models.BooleanField(
        default=True, verbose_name='Слать оповещения о новых коментариях?')

    class Meta(AbstractUser.Meta):
        pass
