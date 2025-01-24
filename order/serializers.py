from rest_framework import serializers
from .models import OrderStatus , ShippingAddress ,  Order
from core.serializers import UserSerializer
from cart.serializers import CartSerializer

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ['id', 'name','deleted']
        extra_kwargs = {"deleted" : {"write_only": True}}



class ShippingAddressGetSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = ShippingAddress
        fields = "__all__"


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class OrderSerializerGet(serializers.ModelSerializer):
    user = UserSerializer()
    cart = CartSerializer()
    shipping_address = ShippingAddressGetSerializer()
    class Meta:
        model = Order
        fields = "__all__"
        depth = 2
       


