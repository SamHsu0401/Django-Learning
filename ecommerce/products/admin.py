from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Product, Order, OrderProduct



class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "date",
        "image"
    ]

class OrderAdmin(admin.ModelAdmin):
    list_display = ["user",
                    "ordered",
                    "quantity"
                    ]



admin.site.register(Product, ProductAdmin)

admin.site.register(Order)
admin.site.register(OrderProduct, OrderAdmin)
