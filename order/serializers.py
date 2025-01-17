from rest_framework import serializers
from .models import OrderStatus

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ['id', 'name','deleted']
        extra_kwargs = {"deleted" : {"write_only": True}}
