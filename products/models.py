from django.db import models

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    desc = models.TextField(blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=False, blank=False)
    image = models.ImageField(upload_to=upload_to, null=True, blank=True)