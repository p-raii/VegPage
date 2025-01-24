from django.shortcuts import render, get_object_or_404, redirect
from .models import Vegetable

# Display the list of vegetables and handle search functionality
def vegetable_list(request):
    query = request.GET.get('q', '')  # Get search query from the request
    vegetables = Vegetable.objects.filter(available=True)  # Only show available vegetables

    if query:
        vegetables = vegetables.filter(name__icontains=query)  # Search by name (case-insensitive)

    context = {
        'vegetables': vegetables,
        'query': query,  # To show the current search query in the template
    }
    print("here")
    return render(request, 'vegproduct/vegetable_list.html', context)

# Add an item to the cart
def add_to_cart(request, pk):
    vegetable = get_object_or_404(Vegetable, pk=pk)
    cart = request.session.get('cart', {})  # Get the cart from session (initialize if not present)

    # Add or update the vegetable in the cart
    if str(pk) in cart:
        cart[str(pk)]['quantity'] += 1  # Increase quantity if already in cart
    else:
        cart[str(pk)] = {
            'name': vegetable.name,
            'price': str(vegetable.price),  # Convert Decimal to string for session storage
            'quantity': 1,
        }

    request.session['cart'] = cart  # Save the updated cart back to session
    return redirect('vegetable_list')  # Redirect back to the vegetable list
