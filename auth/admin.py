from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_customer', 'is_admin_user', 'is_active')
    list_filter = ('is_customer', 'is_admin_user')
    search_fields = ('username', 'email')
