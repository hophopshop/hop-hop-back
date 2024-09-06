from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from authentication.managers import UserManager


class Customer(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    phone_number = models.CharField(_("phone number"), max_length=17, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class CustomerAddress(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='shipping_info', primary_key=True)
    shipping_country = models.CharField(max_length=100)
    shipping_city = models.CharField(max_length=100)
    shipping_address = models.CharField(max_length=255)
    shipping_postcode = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.shipping_address}, {self.shipping_city}, {self.shipping_country}"
