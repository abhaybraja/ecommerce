from django.test import TestCase
from .models import Product, CartItem, Order
from django.urls import reverse
import uuid
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from store.models import Product

User = get_user_model()

class EcommerceTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        # Create a customer user
        self.user = User.objects.create_user(username="cust1", password="testpass", is_customer=True)
        
        # Authenticate the user
        response = self.client.post("/api/token/", {
            "username": "cust1",
            "password": "testpass"
        }, format="json")
        access = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")

        # Create a product
        self.item = Product.objects.create(name="Sample Item", price=100, mrp=110)
        self.cart_id = uuid.uuid4()

    def test_add_to_cart(self):
        res = self.client.post("/api/store/cart/add/", {
            "item_id": self.item.id,
            "quantity": 2
        }, format="json")
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['item'], self.item.id)
        self.assertEqual(res.data['quantity'], 2)


    def test_view_cart(self):
        
        CartItem.objects.create(
            user=self.user,
            cart_id=self.cart_id,
            item=self.item,
            quantity=1
        )

        res = self.client.get(f"/api/store/cart/view/{self.cart_id}/")
        self.assertEqual(res.status_code, 200)
        self.assertIn('total', res.json())

    def test_checkout_without_code(self):
        CartItem.objects.create(
            user=self.user,
            cart_id=self.cart_id,
            item=self.item,
            quantity=1
        )
        res = self.client.post("/api/store/checkout/", {
            "cart_id": str(self.cart_id)
        }, content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_discount_generation(self):
        orders = []
        for i in range(5):  # make 5 orders to trigger nth condition
            orders.append(
                Order(cart_id=uuid.uuid4(), total_amount=100, discount_amount=0, user=self.user)
            )
        Order.objects.bulk_create(orders)
        res = self.client.post("/api/store/admin/generate-discount/")
        self.assertEqual(res.status_code, 200)
        self.assertIn("code", res.json())
