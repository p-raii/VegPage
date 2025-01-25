from django.urls import path
from . import views


urlpatterns = [
    path('add/<int:vegetable_id>/', views.add_to_cart, name='add_to_cart'),
    path('view/', views.view_cart, name='view_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),
]

