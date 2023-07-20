from django.db import models
from django.conf import settings
from django.urls import reverse



class Product(models.Model):
    title = models.CharField(max_length= 100)
    description = models.TextField()
    price = models.FloatField(default=0)
    
    
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
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    
        
    
    
    
    