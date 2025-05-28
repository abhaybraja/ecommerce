from django.contrib import admin
from .models import CartItem, Order, DiscountCode

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'item', 'quantity')
    search_fields = ('cart_id',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart_id', 'total_amount', 'discount_code', 'discount_amount', 'created_at')
    search_fields = ('cart_id', 'discount_code')

@admin.register(DiscountCode)
class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'is_used', 'order_number')
    search_fields = ('code',)
