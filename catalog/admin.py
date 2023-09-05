from django.contrib import admin
from catalog.models import Product, Category


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'product_price', 'product_category',)
    list_filter = ('product_category',)
    search_fields = ('product_name', 'product_description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_description',)
    list_filter = ('category_name',)
    search_fields = ('category_name',)
