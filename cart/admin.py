from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'created_at', 'is_new')
    list_filter = ('is_new',)  # Filter orders by new status
    search_fields = ('user__username',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # Highlight new orders
        queryset = queryset.filter(is_new=True)  # This shows only new orders by default
        return queryset
