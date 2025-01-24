from django.urls import path
from . import views

urlpatterns = [
    path('', views.vegetable_list, name='vegetable_list'),  # List and search vegetables
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),  # Add vegetable to cart
]
