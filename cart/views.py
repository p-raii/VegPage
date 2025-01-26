# cart/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from .models import Order
from vegproduct.models import Vegetable
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def add_to_cart(request, vegetable_id):
    vegetable = get_object_or_404(Vegetable, id=vegetable_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, vegetable=vegetable)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('view_cart')

@login_required
def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if request.method == "POST":
        cart_item.quantity = int(request.POST.get('quantity', 1))
        cart_item.save()
    return redirect('view_cart')



@login_required
def checkout(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        if not phone_number or not address:
            return render(request, 'cart/checkout.html', {'error': "Phone number and address are required!"})
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.quantity * item.vegetable.price for item in cart_items)

        # Collect item details
        item_list = []
        for item in cart_items:
            item_list.append({
                'name': item.vegetable.name,
                'quantity': item.quantity
            })

        # Create an order
        order = Order.objects.create(
            user=request.user,
            total_price=total_price,
            phone_number=phone_number,
            address=address,
            items=item_list
        )

        # Move items from cart to order (optional logic to handle cart items)

        cart_items.delete()  # Clear the cart after order is placed

        return redirect('view_cart') # Replace with your success page

    return render(request, 'cart/checkout.html')

