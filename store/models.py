from django.db import models
import uuid
from django.conf import settings

from inventory.models import Product

# Create your models here.

class CartItem(models.Model):
    cart_id = models.UUIDField(default=uuid.uuid4, db_index=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart_items")
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Order(models.Model):
    cart_id = models.UUIDField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_code = models.CharField(max_length=50, null=True, blank=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

class DiscountCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    is_used = models.BooleanField(default=False)
    order_number = models.PositiveIntegerField()  # nth order that triggered this
