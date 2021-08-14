from django.contrib.auth import get_user_model
from django.db import models
from product.models import Product

User = get_user_model()

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_items = models.IntegerField(default=0)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()


