from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import Signal


from .utilities import send_activation_notification


user_registrated = Signal(providing_args=['instance'])


def user_registrated_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])


user_registrated.connect(user_registrated_dispatcher)


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(
        default=False, db_index=True, verbose_name='Прошел активацию?')
    send_message = models.BooleanField(
        default=True, verbose_name='Слать оповещения о новых коментариях?')

    class Meta(AbstractUser.Meta):
        pass
