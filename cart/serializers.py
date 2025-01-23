from .models import Cart
from core.serializers import UserSerializer
from product.serializers import ProductGetSerializer
from rest_framework import serializers


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    product = ProductGetSerializer()
    class Meta:
        model = Cart
        fields = "__all__"

class PostCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = "__all__"