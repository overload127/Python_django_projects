from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render


def index(request):
    template = 'main/index.html'

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


def login(request):
    template = 'main/login.html'
    if request.method == 'POST':
        pass
    else:
        pass
    context = {
    }
    return render(request, template, context)


def logout(request):
    template = 'main/logout.html'
    context = {
    }
    return render(request, template, context)


def registration(request):
    template = 'main/registration.html'
    context = {
    }
    return render(request, template, context)