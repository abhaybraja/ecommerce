from auth_service.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
class ProfileView(APIView):
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("Authorization"))
    def get(self, request, format=None):
        profile = UserSerializer(request.user).data
        return Response(profile)