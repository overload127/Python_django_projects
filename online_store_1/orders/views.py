
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User

from .models import ProductInBasket, ProductInOrder, Order
from .forms import CheckoutContactForm


def basket_adding(request):
    print('ok')
    return_dict = dict()
    session_key = request.session.session_key
    product_id = request.POST.get('product_id')
    number = request.POST.get('number')
    is_delete = request.POST.get('is_delete')

    if is_delete == 'true':
        ProductInBasket.objects.filter(id=product_id).update(is_active=False)
    else:
        current_product, created = ProductInBasket.objects.get_or_create(
            session_key=session_key, product_id=product_id, is_active=True,
            defaults={'number': int(number)})
        if not created:
            current_product.number += int(number)
            current_product.save(force_update=True)

    # common code for 2 cases
    items_in_basket = ProductInBasket.objects.filter(
        session_key=session_key, is_active=True)
    products_total_number = 0
    list_of_all_positions = list()
    for item in items_in_basket:
        products_total_number += item.number
        current_product = dict()
        current_product['id'] = item.id
        current_product['product_name'] = item.product.name
        current_product['number'] = item.number
        current_product['product_price'] = item.product.price
        list_of_all_positions.append(current_product)

    return_dict['products_total_number'] = products_total_number
    return_dict['list_of_all_positions'] = list_of_all_positions
    return JsonResponse(return_dict)


def checkout(request):
    template = 'orders/checkout.html'
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(
        session_key=session_key, is_active=True)
    list_product = list()
    for element in products_in_basket:
        product_in_bascket = dict()
        product_in_bascket['id'] = element.id
        product_in_bascket['name'] = element.product.name
        product_in_bascket['number'] = element.number
        product_in_bascket['price'] = element.product.price
        product_in_bascket['total_price'] = element.product.price * element.number
        list_product.append(product_in_bascket)
    form = CheckoutContactForm(request.POST or None)
    
    if request.method == 'POST':
        print("ok1")
        if form.is_valid():
            data = request.POST
            name = data['name']
            phone = data['phone']
            user, create = User.objects.get_or_create(
                username=phone, defaults={'first_name': name})

            order = Order.objects.create(
                user=user, customer_name=name, customer_phone=phone,
                status_id=5
            )
            for name, value in data.items():
                if name.startswith('product_in_basket_'):
                    product_in_basket_id = int(name.split('product_in_basket_')[1])
                    product_in_basket = ProductInBasket.objects.get(
                        id=product_in_basket_id)

                    price = product_in_basket.product.price
                    number = int(value)
                    ProductInOrder.objects.create(
                        product=product_in_basket.product,
                        number=number,
                        price_per_item=price,
                        total_price=price*number,
                        order=order
                    )
            ProductInBasket.objects.filter(
                session_key=session_key, is_active=True).update(
                    is_active=False)
            list_product = []
        else:
            pass
    else:
        pass
    context = {'products_in_basket': list_product,
               'form': form}
    return render(request, template, context=context)
