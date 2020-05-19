from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.shortcuts import HttpResponsePermanentRedirect
from django.http import HttpResponseNotModified, HttpResponseBadRequest
from django.http import HttpResponseForbidden, HttpResponseNotFound
from django.http import HttpResponseNotAllowed, HttpResponseGone
from django.http import HttpResponseServerError
from django.shortcuts import render
from django.template.response import TemplateResponse

from . import forms, models


def index(request):
    if request.method == 'POST':
        userform = forms.UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data['name']
            age = userform.cleaned_data['age']
            return HttpResponse(f'<h2>Hello {name}!</h2><p>Тебе уже {age} лет!</p>')
    else:
        userform = forms.UserForm()
    langs = ['English', 'German', 'French', 'Spanish', 'Chinese']
    data = {'n': 5, 'langs': langs, 'userform': userform}
    return TemplateResponse(request, 'index.html', context=data)


def index2(request):
    header = 'Personal Data'                    # обычная переменная
    langs = ['English', 'German', 'Spanish']    # массив
    user = {'name': 'Tom', 'age': 23}           # словарь
    addr = ('Абрикосовая', 23, 45)              # кортеж

    data = {'header': header, 'langs': langs, 'user': user, 'address': addr}
    return TemplateResponse(request, 'firstapp/home.html', context=data)


def index3(request):
    people = models.Person.objects.all()
    return render(request, 'index3.html', {'people': people})


def create(request):
    if request.method == 'POST':
        tom = models.Person()
        tom.name = request.POST.get('name')
        tom.age = request.POST.get('age')
        tom.save()
    return HttpResponseRedirect('/index3/')


def edit(request, _id):
    try:
        person = models.Person.objects.get(id=_id)

        if request.method == 'POST':
            person.name = request.POST.get('name')
            person.age = request.POST.get('age')
            person.save()
            return HttpResponseRedirect('/index3/')
        else:
            return render(request, 'edit.html', {'person': person})
    except models.Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Person not found</h2>')


def delete(request, _id):
    try:
        person = models.Person.objects.get(id=_id)

        person.delete()
        return HttpResponseRedirect('/index3/')
    except models.Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Person not found</h2>')

def contact(request):
    data = {}
    return TemplateResponse(request, 'firstapp/contact.html', context=data)


def details(request):
    return HttpResponsePermanentRedirect('/')


def products(request, productid=21):
    oytput = f'<h2>Product № {productid}</h2>'
    return HttpResponse(oytput)


def users(request, _id=1, name='Bob'):
    output = f'<h2>User</h2><h3>id: {_id} name: {name}'
    return HttpResponse(output)


def board(request, boardid):
    category = request.GET.get('cat', '')
    oytput = f'<h2>Board № {boardid} Category: {category}</h2>'
    return HttpResponse(oytput)


def cases(request):
    _id = request.GET.get('id', 1)
    name = request.GET.get('name', 'Tom')
    output = f'<h2>User</h2><h3>id: {_id} name: {name}'
    return HttpResponse(output)


def m304(request):
    return HttpResponseNotModified()


def m400(request):
    return HttpResponseBadRequest('<h2>Bad Request</h2>')


def m403(request):
    return HttpResponseForbidden('<h2>Not Found</h2>')


def m404(request):
    return HttpResponseNotFound('<h2>Not Found</h2>')


def m405(request):
    return HttpResponseNotAllowed('<h2>Method is not allowed</h2>')


def m410(request):
    return HttpResponseGone('<h2>Content is no longer here</h2>')


def m500(request):
    return HttpResponseServerError('<h2>Something is wrong</h2>')


def fun(request, count):
    if count <= 1:
        return HttpResponse('уже 1')
    print(count)
    count -= 1
    return HttpResponseRedirect(f'/fun/{count}')


def fun2(request, count):
    elements = [i for i in range(count)]
    context = {'elements': elements}
    return TemplateResponse(request, 'fun2.html', context=context)
