from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from inventory.serializers import ProductSerializer
from .models import Product
# Create your views here.

class ProductAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request):
        products = Product.objects.all()
        data = ProductSerializer(products,many=True).data
        return Response(data)