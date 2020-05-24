from .models import ProductInBasket


def getting_basket_info(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    items_in_basket = ProductInBasket.objects.filter(
        session_key=session_key, is_active=True)
    products_total_number = 0
    for item in items_in_basket:
        products_total_number += item.number

    return {
        'items_in_basket': items_in_basket,
        'products_total_number': products_total_number,
    }
