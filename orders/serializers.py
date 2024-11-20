from rest_framework import serializers
from .models import Order, OrderProduct
from products.models import Product
from products.serializers import ProductSerializer

class OrderProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['bread', 'quantity']  # Accept only bread ID and quantity


class OrderProductRetrieveSerializer(serializers.ModelSerializer):
    bread = ProductSerializer()  # Populate with Product details

    class Meta:
        model = OrderProduct
        fields = ['bread', 'quantity']  # Include bread details and quantity



class OrderSerializer(serializers.ModelSerializer):
    # Dynamically set serializers for order_products
    order_products = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'total_price', 'created_at', 'message', 'order_products']
        read_only_fields = ['id', 'created_at']

    def get_order_products(self, obj):
        # Use the output serializer for retrieving data
        return OrderProductRetrieveSerializer(obj.order_products.all(), many=True).data

    def create(self, validated_data):
        # Handle nested order products for creation
        order_products_data = self.context['request'].data.get('order_products', [])
        order = Order.objects.create(**validated_data)

        for product_data in order_products_data:
            # Bread is passed as an ID
            bread_id = product_data['bread']
            quantity = product_data['quantity']
            bread = Product.objects.get(id=bread_id)  # Ensure bread exists in the DB
            OrderProduct.objects.create(order=order, bread=bread, quantity=quantity)

        return order
