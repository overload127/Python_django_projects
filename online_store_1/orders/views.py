from django.shortcuts import render
from django.http import JsonResponse

from .models import ProductInBasket


def basket_adding(request):
    print("ok")
    return_dict = dict()
    session_key = request.session.session_key
    product_id = request.POST.get('product_id')
    number = request.POST.get('number')
    new_product = ProductInBasket.objects.create(
        session_key=session_key, product_id=product_id, number=number)
    items_in_basket = ProductInBasket.objects.filter(
        session_key=session_key, is_active=True)
    products_total_number = 0
    for item in items_in_basket:
        products_total_number += item.number
    return_dict['products_total_number'] = products_total_number
    return JsonResponse(return_dict)
