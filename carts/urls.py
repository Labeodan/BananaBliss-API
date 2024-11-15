from django.urls import path
from .views import CartListView, CartDetailView, CartProductListView, CartProductDetailView

urlpatterns = [
    # Cart-related endpoints
    path('', CartListView.as_view(), name='cart-list'),  # List and create carts
    path('<int:pk>/', CartDetailView.as_view(), name='cart-detail'),  # Get, update, delete a specific cart

    # CartProduct-related endpoints
    path('<int:cart_id>/products/', CartProductListView.as_view(), name='cart-product-list'),  # List and add products to a cart
    path('<int:cart_id>/products/<int:pk>/', CartProductDetailView.as_view(), name='cart-product-detail'),  # Get, update, delete a specific product in the cart
]
