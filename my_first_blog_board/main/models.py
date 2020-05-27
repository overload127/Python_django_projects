from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(
        default=False, db_index=True, verbose_name='Прошел активацию?')
    send_message = models.BooleanField(
        default=True, verbose_name='Слать оповещения о новых коментариях?')
    lessons = models.ManyToManyField(
        'Lesson', through='FollowerOfLesson', related_name='+',
        verbose_name='Доступные уроки')

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Lesson(models.Model):
    title = models.CharField(
        max_length=250, verbose_name='Название урока')
    followers = models.ManyToManyField(
        'AdvUser', through='FollowerOfLesson', related_name='+',
        verbose_name='Подписчики на урок')
    author = models.ForeignKey(
        AdvUser, blank=True, null=True, default=None,
        on_delete=models.SET_NULL, verbose_name='Автор урока')
    created = models.DateTimeField(
        auto_now_add=False, auto_now=False, default=timezone.now,
        verbose_name='Создан')
    update = models.DateTimeField(
        auto_now_add=False, auto_now=True, verbose_name='Изменен')
    published = models.DateTimeField(
        auto_now_add=False, db_index=True, blank=True, null=True,
        verbose_name='Опубликовано')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Уроки'
        verbose_name = 'Урок'


class FollowerOfLesson(models.Model):
    user = models.ForeignKey(AdvUser, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.lesson}'

    class Meta:
        db_table = 'follower_of_lesson'


class LesonTube(models.Model):
    title = models.CharField(
        max_length=250, db_index=True, verbose_name='Название видео-урока')
    author = models.ForeignKey(
        AdvUser, null=True, default=None, on_delete=models.SET_NULL,
        verbose_name='Автор урока')
    path_file = models.FileField(max_length=100, verbose_name='Видео-урок')
    created = models.DateTimeField(
        auto_now_add=False, auto_now=False, default=timezone.now,
        verbose_name='Создан')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Видео-уроки'
        verbose_name = 'Видео-урок'
