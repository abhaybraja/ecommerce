from rest_framework.permissions import BasePermission

class IsCustomer(BasePermission):
    def has_permission(self, request):
        return request.user and request.user.is_authenticated and request.user.is_customer

class IsAdminUser(BasePermission):
    def has_permission(self, request):
        return request.user and request.user.is_authenticated and request.user.is_admin_user
