from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsAdminOrOwner

class OrderListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrOwner]
    serializer_class = OrderSerializer

    def get_queryset(self):
        # Admin can see all orders; users can only see their own orders
        if self.request.user.role == 'admin':
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)



class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrOwner]  # Using custom permission
    serializer_class = OrderSerializer

    def get_queryset(self):
        # Admin can see all orders, users can only see their own orders
        if self.request.user.role == 'admin':
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)

    def get_object(self):
        # Admin can view any order; users can only view their own
        obj = super().get_object()
        if obj.user != self.request.user and self.request.user.role != 'admin':
            raise NotFound("Order not found")
        return obj
