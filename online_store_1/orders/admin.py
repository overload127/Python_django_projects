from django.contrib import admin
from .models import Status, Order, ProductInOrder, ProductInBasket


class ProductImageInLine(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]
    search_fields = ['name']
    list_filter = ['is_active']

    class Meta:
        model = Order


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    search_fields = ['customer_name', 'customer_email', 'customer_phone',
                     'comments']
    list_filter = ['status']
    inlines = [ProductImageInLine]

    class Meta:
        model = Order


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]
    list_filter = ['order', 'product', 'is_active']

    class Meta:
        model = ProductInOrder


class ProductInBasketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInBasket._meta.fields]
    list_filter = ['order', 'product', 'is_active']

    class Meta:
        model = ProductInBasket


admin.site.register(Status, StatusAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductInOrder, ProductInOrderAdmin)
admin.site.register(ProductInBasket, ProductInBasketAdmin)
