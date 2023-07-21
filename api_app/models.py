#https://stackabuse.com/creating-a-rest-api-with-django-rest-framework/

from django.db import models

# Create your models here.

class CartItem(models.Model):   #PascalCase  #Model is superclass cartitem is childclass
      product_name=models.CharField(max_length=200)
      product_price = models.FloatField()   #positive as well as negative values
      product_quantity = models.PositiveIntegerField()   #range starts from +0 no nigative value
      
      
      pass

