from django.test import TestCase
from .models import Product, CartItem, Order, DiscountCode
from django.urls import reverse
import uuid

class EcommerceTests(TestCase):
    def setUp(self):
        self.item = Product.objects.create(name="Sample Item", price=100, mrp=110)
        self.cart_id = uuid.uuid4()

    def test_add_to_cart(self):
        res = self.client.post("/cart/add/", {
            "cart_id": str(self.cart_id),
            "item": self.item.id,
            "quantity": 2
        }, content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_view_cart(self):
        CartItem.objects.create(cart_id=self.cart_id, item=self.item, quantity=1)
        res = self.client.get(f"/cart/view/{self.cart_id}/")
        self.assertEqual(res.status_code, 200)
        self.assertIn('total', res.json())

    def test_checkout_without_code(self):
        CartItem.objects.create(cart_id=self.cart_id, item=self.item, quantity=1)
        res = self.client.post("/checkout/", {
            "cart_id": str(self.cart_id)
        }, content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_discount_generation(self):
        orders = []
        for i in range(5):  # make 5 orders to trigger nth condition
            orders.append(
                Order(cart_id=uuid.uuid4(), total_amount=100, discount_amount=0)
            )
        Order.objects.bulk_create(orders)
        res = self.client.post("/admin/generate-discount/")
        self.assertEqual(res.status_code, 200)
        self.assertIn("code", res.json())
