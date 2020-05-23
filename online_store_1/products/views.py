from django.shortcuts import render, get_object_or_404

from products.models import Product, ProductImage


def product(request, product_id):
    template = 'products/product.html'
    product = get_object_or_404(Product, id=product_id)
    product_images = ProductImage.objects.filter(
        product=product_id, is_active=True)
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print(session_key)
    content = {'product': product,
               'product_images': product_images,
               'session_key': session_key}
    return render(request, template, context=content)
