from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from .validators import validate_mp4
from django.db import models
from django.utils import timezone
from django.conf import settings

from .utilities import get_timestamp_path


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(
        default=False, db_index=True, verbose_name='Прошел активацию?')
    send_message = models.BooleanField(
        default=True, verbose_name='Слать оповещения о новых коментариях?')
    lessons = models.ManyToManyField(
        'Lesson', blank=True,
        verbose_name='Доступные уроки')

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Lesson(models.Model):
    title = models.CharField(
        max_length=250, verbose_name='Название урока')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, default=None,
        on_delete=models.SET_NULL,
        verbose_name='Автор урока')
    created = models.DateTimeField(
        auto_now_add=False, auto_now=False, default=timezone.now,
        verbose_name='Создан')
    update = models.DateTimeField(
        auto_now_add=False, db_index=True, auto_now=True,
        verbose_name='Изменен')
    published = models.DateTimeField(
        auto_now_add=False, db_index=True, blank=True, null=True,
        verbose_name='Опубликовано')
    is_active = models.BooleanField(
        default=True, db_index=True, verbose_name='Выводить в списке?')
    lessons_video = models.ManyToManyField(
        'LessonVideo', blank=True,
        verbose_name='Видео-уроки')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Уроки'
        verbose_name = 'Урок'


class LessonVideo(models.Model):
    # Fixde it размер видоса ограничить каким-нибудь нормальнымразмером.
    title = models.CharField(
        max_length=250, verbose_name='Название видео-урока')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, default=None,
        on_delete=models.SET_NULL,
        verbose_name='Автор урока')
    video_path = models.FileField(
        max_length=100, upload_to=get_timestamp_path,
        validators=[FileExtensionValidator(['mp4']), validate_mp4],
        verbose_name='Видео-урок')
    is_active = models.BooleanField(
        default=True, db_index=True, verbose_name='Выводить в списке?')
    created = models.DateTimeField(
        auto_now_add=False, auto_now=False, default=timezone.now,
        db_index=True, verbose_name='Создан')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Видео-уроки'
        verbose_name = 'Видео-урок'
