# accounts/models.py

from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(blank=True, null=True, default="+1")
    

    