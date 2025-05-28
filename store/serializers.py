from rest_framework import serializers
from .models import CartItem, Order, DiscountCode

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'user', 'cart_id', 'item', 'quantity']
        read_only_fields = ['user']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'cart_id', 'total_amount', 'discount_code', 'discount_amount','created_at', 'order_status']

class DiscountCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountCode
        fields = '__all__'
