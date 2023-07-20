# accounts/models.py
#https://django-phonenumber-field.readthedocs.io/en/latest/reference.html#form-field
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField(blank=True, null=True, default="+1")
    

    