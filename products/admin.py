from django.contrib import admin
from .models import Product, Category, Brand
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'price')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Brand)
