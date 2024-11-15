from rest_framework import generics, status
from rest_framework.response import Response
from .models import Cart, CartProduct
from .serializers import CartSerializer, CartProductSerializer
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.permissions import IsAuthenticated

# View to list all carts for the logged-in user
class CartListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        # Return carts for the current logged-in user
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Set the user to the current logged-in user when creating a cart
        serializer.save(user=self.request.user)

# View to retrieve a specific cart
class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)  # Ensure that users can only access their carts

# View to list all products in the cart
class CartProductListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer

    def get_queryset(self):
        cart_id = self.kwargs['cart_id']
        return CartProduct.objects.filter(cart_id=cart_id)  # Return products for the given cart

    def perform_create(self, serializer):
        cart_id = self.kwargs['cart_id']
        cart = Cart.objects.get(id=cart_id)
        serializer.save(cart=cart)

# View to update or delete a specific product in a cart
class CartProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer

    def get_queryset(self):
        cart_id = self.kwargs['cart_id']
        return CartProduct.objects.filter(cart_id=cart_id)  # Only show products for the given cart
