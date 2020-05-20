from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.views import (
    LoginView, LogoutView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .models import AdvUser
from .forms import (
    RegisterAdvUserForm, AdvUserForm, ChangeAdvUserInfoForm)


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
    template_name = 'main/profile.html'
    context = {}
    return render(request, template_name, context)


class AdvUserRegisterView(CreateView):
    model = AdvUser
    template_name = 'main/register_page.html'
    success_url = reverse_lazy('main:home')
    form_class = RegisterAdvUserForm
    success_message = 'Пользователь успешно создан'


class AdvUserLoginView(LoginView):
    template_name = 'main/login.html'
    form_class = AdvUserForm
    success_url = reverse_lazy('main:home')


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
