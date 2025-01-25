from django.shortcuts import render, get_object_or_404, redirect
from .models import Vegetable
from django.db.models import Q

# Display the list of vegetables and handle search functionality
def vegetable_list(request):
    query = request.GET.get('q', '')  # Get search query from the request
    vegetables = Vegetable.objects.filter(available=True)  # Only show available vegetables

    if query:
        vegetables = vegetables.filter(Q(name__icontains=query) | Q(category__icontains=query))  # Search by name (case-insensitive)

    context = {
        'vegetables': vegetables,
        'query': query,  # To show the current search query in the template
    }
    return render(request, 'vegproduct/vegetable_list.html', context)



