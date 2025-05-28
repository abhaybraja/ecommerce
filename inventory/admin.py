from django.contrib import admin
from .models import Product

@admin.register(Product)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'mrp')
    search_fields = ('name',)