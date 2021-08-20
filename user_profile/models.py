from django.contrib.auth import get_user_model
from django.db import models
from orders.countries import Countries

User = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=255, default='')
    address_line_2 = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=255, default='')
    state_province_region = models.CharField(max_length=255, default='')
    zipcode = models.CharField(max_length=20, default='')
    telephone_number = models.CharField(max_length=255, default='')
    country_region = models.CharField(max_length=255, choices=Countries.choices, default=Countries.Canada)

    def __str__(self):
        return self.address_line_1
