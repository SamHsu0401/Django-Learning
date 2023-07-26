#/Users/samhsu/Desktop/Personal Learning/Python learning/Django-learning/ecommerce/products/models.py
from django.db import models
from django.conf import settings
from django.urls import reverse



class Product(models.Model):
    title = models.CharField(max_length= 100)
    description = models.TextField()
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to="uploads/products_images/", blank=True, null=True)
    
    
    
    CATEGORY_CHOICE = [
        ("NONE", "Not categorized yet"),
        ("ELEC", "Electronics"),
        ("FASH", "Fashion and Apprael"),
        ("HOME", "Home and Kitchen"),
    ]
    
    category = models.CharField(
        max_length= 4,
        choices= CATEGORY_CHOICE,
        default= "NONE"
    )
    
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})
    
    def get_add_to_cart_url(self):
        return reverse("add_to_cart", kwargs={
            'pk': self.pk
        })
    def get_remove_to_cart_url(self):
        return reverse("remove_item_from_cart", kwargs={
        'pk': self.pk
    })
        

    
class OrderProduct(models.Model):
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    
    
    
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} of {self.product.title}"
    


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    products = models.ManyToManyField(OrderProduct)
    start_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField (max_length=50, default='', blank=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    
    def totalItems(self):
        total_items = 0
        for order_product in self.products.all():
            total_items += order_product.quantity
        return total_items

    def __str__(self):
        return f"Order #{self.pk} - Total Items: {self.totalItems()}"

    
        
    
    
    
    