from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'created_at', 'is_new','phone_number', 'address','status')
    def formatted_items(self, obj):
        # Format the list of items (name and quantity)
        item_display = ", ".join([f"{item['name']} (x{item['quantity']})" for item in obj.items])
        return item_display
    formatted_items.short_description = 'Items Ordered'
    list_filter = ('is_new',)  # Filter orders by new status
    search_fields = ('user__username',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # Highlight new orders
        queryset = queryset.filter(is_new=True)  # This shows only new orders by default
        return queryset
