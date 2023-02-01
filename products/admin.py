from django.contrib import admin
from .models import Product, Category, Brand, UserReview
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'price')

class UserReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'review', 'rating')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(UserReview, UserReviewAdmin)
