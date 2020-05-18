from django.shortcuts import render


def index(request):
    template = 'main/index.html'
    context = {}
    return render(request, template, context)
