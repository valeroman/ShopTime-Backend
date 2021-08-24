from django.contrib.auth import get_user_model
from django.db import models
from product.models import Product

User = get_user_model()

class WishList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_items = models.IntegerField(default=0)

class WishListItem(models.Model):
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

