from django.shortcuts import render
from . import forms

from products.models import ProductImage


def landing(request):
    form = forms.SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        new_form = form.save()
    return render(request, 'landing/landing.html', context=locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_apple = products_images.filter(product__category__id=2)
    products_images_mehan = products_images.filter(product__category__id=1)
    return render(request, 'landing/home.html', context=locals())
