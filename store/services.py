from .models import Order, DiscountCode, CartItem
from django.utils.crypto import get_random_string

NTH_ORDER = 5

def generate_discount_if_eligible():
    order_count = Order.objects.count()
    if order_count % NTH_ORDER == 0:
        code = get_random_string(10).upper()
        DiscountCode.objects.create(code=code, order_number=order_count)
        return {"code": code, "message": "Discount code generated"}
    return {"message": "Not eligible yet"}

def get_analytics_summary():
    total_items = sum([i.quantity for i in CartItem.objects.all()])
    total_amount = sum([o.total_amount + o.discount_amount for o in Order.objects.all()])
    discount_codes = DiscountCode.objects.values_list("code", flat=True)
    total_discount = sum([o.discount_amount for o in Order.objects.all()])

    return {
        "total_items_purchased": total_items,
        "total_purchase_amount": float(total_amount),
        "discount_codes": list(discount_codes),
        "total_discount_given": float(total_discount)
    }
