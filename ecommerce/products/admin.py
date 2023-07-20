from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Product



class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "date",
    ]




admin.site.register(Product, ProductAdmin)