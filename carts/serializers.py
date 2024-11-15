from rest_framework import serializers
from .models import Cart, CartProduct
from products.models import Product  # Assuming Product model is in the 'products' app
from django.contrib.auth import get_user_model
User = get_user_model()

# CartProduct serializer
class CartProductSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)  # Include product name

    class Meta:
        model = CartProduct
        fields = ['id', 'product', 'product_name', 'quantity']

# Cart serializer
class CartSerializer(serializers.ModelSerializer):
    user_email = serializers.CharField(source='user.email', read_only=True)  # Include user email
    cart_products = CartProductSerializer(many=True, read_only=True)  # Nested CartProductSerializer

    class Meta:
        model = Cart
        fields = ['id', 'user_email', 'cart_products', 'created_at', 'updated_at']
