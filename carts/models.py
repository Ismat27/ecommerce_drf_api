from django.db import models
from django.conf import settings

from products.models import Product

# Create your models here.

User = settings.AUTH_USER_MODEL

class CartItem(models.Model):
    item = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    cart = models.ForeignKey('Cart', null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self) -> str:
        return self.item.name

    @property
    def amount(self):
        product_price = self.item.price
        return self.quantity * product_price

class Cart(models.Model):
    is_ordered = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    @property
    def cart_items(self):
        items = self.cartitem_set.all()
        return items
    
    @property
    def total_amount(self):
        items = self.cartitem_set.all()
        amount = 0
        for item in items:
            amount += item.amount
        return amount
