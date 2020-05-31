from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.views import (
    LoginView, LogoutView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView

from .models import AdvUser, Lesson
from .forms import (
    RegisterAdvUserForm, AdvUserForm, ChangeAdvUserInfoForm)
from my_first_blog_board import settings


def home(request):
    template = 'main/home.html'

    if isinstance(request.user, AnonymousUser):
        name = 'Гость'
    elif request.user.first_name:
        name = request.user.first_name
    else:
        name = request.user
    context = {
        'name': name,
    }
    return render(request, template, context)


@login_required
def profile(request):
    template_name = 'main/user_statistic.html'
    context = {}
    return render(request, template_name, context)


@login_required
def profile_all_list_lessons(request):
    template_name = 'main/all_list_lessons.html'

    lessons = Lesson.objects.values(
        'id',
        'title',
        'author__first_name',
        'author__last_name').filter(is_active=True)

    context = {'lessons': list(lessons)}
    return render(request, template_name, context)


@login_required
def profile_buy_list_lessons(request):
    template_name = 'main/buy_list_lessons.html'

    lessons = Lesson.objects.values(
        'id',
        'title',
        'author__first_name',
        'author__last_name').filter(advuser__id=request.user.id,
                                    is_active=True)
    context = {'lessons': list(lessons)}
    return render(request, template_name, context)


@login_required
def lesson_detail(request, pk):
    """ функция делает два независимых запроса.
    Первый запрос находит урок. (если его нет в базе будет 404)
    Второй запрос составляет список пользователей
    """
    template_name = 'main/lesson_detail.html'

    lesson_quert = Lesson.objects.values(
        'title',
        'author__first_name',
        'author__last_name',
        'lessons_video__title',
        'lessons_video__author__first_name',
        'lessons_video__author__last_name',
        'lessons_video__video_path')
    lesson = get_object_or_404(lesson_quert, pk=pk)

    access_lesson = AdvUser.objects.values('id').filter(
        lessons__id=pk, id=request.user.id)

    context = {'lesson': lesson,
               'MEDIA_URL': settings.MEDIA_URL,
               'buy': bool(access_lesson)}
    return render(request, template_name, context)


class AdvUserRegisterView(CreateView):
    model = AdvUser
    template_name = 'main/register_page.html'
    success_url = reverse_lazy('main:register_page_done')
    form_class = RegisterAdvUserForm


class AdvUserRegisterDoneView(TemplateView):
    template_name = 'main/register_done_page.html'


class AdvUserLoginView(LoginView):
    template_name = 'main/login.html'
    form_class = AdvUserForm


class AdvUserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('main:home')


class AdvUserChangeInfoView(LoginRequiredMixin, UpdateView):
    model = AdvUser
    template_name = 'main/change_user_info.html'
    form_class = ChangeAdvUserInfoForm
    success_url = reverse_lazy('main:profile_page')

    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class AdvUserPasswordChangeView(LoginRequiredMixin,
                                PasswordChangeView):
    template_name = 'main/password_change.html'
    success_url = reverse_lazy('main:profile_page')
