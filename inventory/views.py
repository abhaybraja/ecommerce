from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from inventory.serializers import ProductSerializer
from .models import Product
# Create your views here.

class ProductAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        products = Product.objects.all()
        data = ProductSerializer(products,many=True).data
        return Response(data)