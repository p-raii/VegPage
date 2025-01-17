from django.contrib import admin
from .models import Vegetable
# Register your models here.
@admin.register(Vegetable)
class VegetableAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'available', 'updated_at')
    list_filter = ('available', 'category', 'created_at')
    search_fields = ('name', 'description')