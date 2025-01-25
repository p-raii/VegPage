# cart/models.py
from django.db import models
from django.contrib.auth.models import User
from vegproduct.models import Vegetable

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vegetable = models.ForeignKey(Vegetable, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.vegetable.name} - {self.quantity}"

    def total_price(self):
        return self.quantity * self.vegetable.price

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_new = models.BooleanField(default=True)  # Mark new orders as True
    
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
