from rest_framework import serializers
from .models import Order, OrderProduct
from products.serializers import ProductSerializer  # Assuming you have a Product serializer

class OrderProductSerializer(serializers.ModelSerializer):
    bread = ProductSerializer()

    class Meta:
        model = OrderProduct
        fields = ['bread', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'total_price', 'created_at', 'message', 'order_products']
