from django.db import models
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
    
    

    
    
    
    
    
    