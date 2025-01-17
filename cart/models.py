from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='cart')
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product} - {self.quantity}"
