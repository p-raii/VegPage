
# accounts/views.py
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout




# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userdetails:login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'userdetails/register.html', {'form': form})

# Login view
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Get the authenticated user
            auth_login(request, user)  # Log the user in

            # Redirect to the anime list page (or wherever you want to go after login)
            return render(request, 'vegproduct/vegetable_list.html', {'user': user})  # Make sure you have 'anime_list' URL configured
            
    else:
        form = AuthenticationForm()

    return render(request, 'userdetails/login.html', {'form': form})
   


@login_required
def profile(request):
    user = request.user  # Get the currently logged-in user
    # Get the list of favorite anime for the logged-in user
    
    # Pass user info and favorites to the template
    return render(request, 'userdetails/profile.html', {'user': user})

def logout_view(request):
    logout(request)  # This logs the user out
    return redirect('vegproduct:vegetable_list') 