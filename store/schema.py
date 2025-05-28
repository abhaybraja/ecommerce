from rest_framework import serializers

class CartItemSchema(serializers.Serializer):
    item_id = serializers.IntegerField()
    quantity = serializers.IntegerField()