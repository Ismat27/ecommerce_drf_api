from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self) -> str:
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    desc = models.TextField(blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=False, blank=False)
    discounted_price = models.DecimalField(max_digits=15, decimal_places=2, null=False, blank=False)
    in_stock = models.BooleanField(default=True, null=False, blank=False)
    is_flash_sale = models.BooleanField(default=False, null=False, blank=False)
    stock_quantity = models.IntegerField(default=1, null=False, blank=False)
    image = models.ImageField(upload_to=upload_to, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_recommended = models.BooleanField(default=False, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class UserReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.IntegerField(default=0)
    review = models.TextField(blank=True, null=True)
