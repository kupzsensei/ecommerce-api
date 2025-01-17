from django.db import models
from cart.models import Cart
from django.contrib.auth.models import User
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart , on_delete=models.CASCADE)
    status = models.ForeignKey('OrderStatus' , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    note = models.TextField()
    shipping_address = models.ForeignKey('ShippingAddress' , on_delete=models.CASCADE , null=True , blank=True)

    def __str__(self):
        return f'{self.cart} - {self.status}'



class OrderStatus(models.Model):
    name = models.CharField(max_length=200 , unique=True)

    def __str__(self):
        return self.name
    
class ShippingAddress(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    address = models.TextField()


    def __str__(self):
        return f"{self.user} - {self.address}"