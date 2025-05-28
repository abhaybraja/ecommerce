from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from rest_framework.decorators import api_view
from rest_framework.response import Response

from permissions import IsCustomer, IsAdminUser
from store.schema import CartItemSchema
from .models import *
from .serializers import *
from .services import generate_discount_if_eligible, get_analytics_summary
from decimal import Decimal

@api_view(["POST"])
@permission_classes([IsAuthenticated, IsCustomer])
def add_to_cart(request):
    user=request.user
    serializer = CartItemSchema(data=request.data)
    serializer.is_valid(raise_exception=True)
    item_id = serializer.validated_data['item_id']
    quantity = serializer.validated_data['quantity']

    # find active cart_id (not yet checked out)
    existing_cart = CartItem.objects.filter(user=user).order_by('-id').first()
    cart_id = existing_cart.cart_id if existing_cart else uuid.uuid4()

    cart_item = CartItem.objects.create(
        user=user,
        cart_id=cart_id,
        item_id=item_id,
        quantity=quantity,
    )
    return Response(CartItemSerializer(cart_item).data)

@api_view(["GET"])
def view_cart(request, cart_id):
    user = request.user
    items = CartItem.objects.filter(cart_id=cart_id, user=user)
    total = sum(i.item.price * i.quantity for i in items)
    data = CartItemSerializer(items, many=True).data
    return Response({'items': data, 'total': total})

@api_view(["POST"])
def checkout(request):
    user = request.user
    cart_id = request.data.get("cart_id")
    code = request.data.get("discount_code")
    items = CartItem.objects.filter(cart_id=cart_id, user=user)

    total = sum(i.item.price * i.quantity for i in items)
    discount = Decimal("0.00")

    if code:
        try:
            discount_code = DiscountCode.objects.get(code=code, is_used=False)
            discount = total * Decimal("0.10")
            discount_code.is_used = True
            discount_code.save()
        except DiscountCode.DoesNotExist:
            return Response({"error": "Invalid or used discount code"}, status=400)

    order = Order.objects.create(
        cart_id=cart_id,
        user=user,
        total_amount=total - discount,
        discount_code=code if code else None,
        discount_amount=discount
    )
    generate_discount_if_eligible()
    items.delete()  # clear cart
    return Response(OrderSerializer(order).data)

@api_view(["POST"])
def generate_discount(request):
    return Response(generate_discount_if_eligible())

@api_view(["GET"])
@permission_classes([IsAuthenticated, IsAdminUser])
def analytics(request):
    return Response(get_analytics_summary())
