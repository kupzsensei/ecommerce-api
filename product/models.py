from django.db import models
from imageupload.models import ImageUpload

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100 , unique=True)
    description = models.TextField(blank=True , null=True)
    price = models.DecimalField(decimal_places=2 , max_digits=20)
    img = models.ForeignKey(ImageUpload , on_delete=models.CASCADE)

    def __str__(self):
        return self.name