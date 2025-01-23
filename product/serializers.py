from rest_framework import serializers
from .models import Product
from imageupload.serializers import ImageSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id' , 'name' , 'price' , 'description' ]

  

class ProductGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        depth = 1