from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_customer', 'is_admin_user', 'is_active')
    list_filter = ('is_customer', 'is_admin_user', 'is_active', 'is_staff')
    search_fields = ('username', 'email')

    fieldsets = BaseUserAdmin.fieldsets + (
        ('Role Info', {'fields': ('is_customer', 'is_admin_user')}),
    )

    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('is_customer', 'is_admin_user')}),
    )
