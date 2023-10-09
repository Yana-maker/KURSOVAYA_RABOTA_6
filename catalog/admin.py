from django.contrib import admin
from catalog.models import Product, Category, Contacts, Version


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'product_price', 'product_category', 'product_image', 'product_description',)
    list_filter = ('product_name',)
    search_fields = ('pk', 'product_name', 'product_description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    list_filter = ('category_name',)
    search_fields = ('category_name',)


@admin.register(Contacts)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'massage',)
    list_filter = ('name',)
    search_fields = ('name', 'email',)

@admin.register(Version)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'number_version', 'name_version', 'is_current_version',)
    list_filter = ('product_name', 'number_version', 'name_version', 'is_current_version',)
    search_fields = ('product_name', 'number_version', 'name_version',)
