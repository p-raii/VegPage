from django.conf import settings
from django.db import models
from django.utils import timezone

class Vegetable(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Name of the vegetable
    description = models.TextField(blank=True)  # Optional description of the vegetable
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price per unit (e.g., per kg)
    stock = models.PositiveIntegerField(default=0)  # Quantity available in stock
    image = models.ImageField(upload_to='images/vegetables/', blank=True, null=True)  # Image of the vegetable
    category = models.CharField(max_length=50, blank=True)  # Category (e.g., leafy, root, fruit)
    available = models.BooleanField(default=True)  # Whether the vegetable is currently available
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the product was added
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for the last update

    def __str__(self):
        return self.name