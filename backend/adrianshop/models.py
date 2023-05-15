from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField


# Create your models here.

class APIUser(AbstractUser):
    pass

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=300, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    product_image = models.FileField(upload_to='products/%Y/%b/')
    class ProductTag(models.TextChoices):
        HAT = 'Hats'
        SHIRT = 'Shirts'
        HOODIE = 'Hoodies'
        TROUSER = 'Trousers'
        MISC = 'Miscellaneous'
    product_tag = models.CharField(max_length=13, choices=ProductTag.choices, default=ProductTag.MISC)

class Basket(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(APIUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    date_made = models.DateTimeField(auto_now_add=True)

class BasketItem(models.Model):
    id = models.AutoField(primary_key=True)
    basket_id = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    def item_price(self):
        return self.product_id.price * self.quantity

    def product_name(self):
        return self.product_id.name

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    basket_id = models.ForeignKey(Basket, on_delete=models.CASCADE)
    user_id = models.ForeignKey(APIUser, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    shipping_address = models.TextField(default='')