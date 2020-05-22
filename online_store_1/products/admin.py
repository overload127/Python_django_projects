from django.contrib import admin

from .models import Product, ProductImage


class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    search_fields = ['name', 'description']
    list_filter = ['is_active']
    inlines = [ProductImageInLine]

    class Meta:
        model = Product


class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]
    search_fields = ['product', 'image']
    list_filter = ['is_active']

    class Meta:
        model = ProductImage


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
