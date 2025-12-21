from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not email or not password:
            messages.error(request, "Please fill in all required fields")
            return redirect('register')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('register')


        try:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            
            messages.success(request, 'Account created! You can now log in.')
            return redirect('login')
        except Exception as e:
            messages.error(request, "An error occurred during registration")
            return redirect('register')
            
    return render(request, 'register.html')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:

            user = User.objects.get(email=email)
            if user.check_password(password):
                login(request, user)
                
                name = user.first_name if user.first_name else "Traveler"
                messages.success(request, f"Welcome back, {name}!")
                
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('index')
            else:
                messages.error(request, "Invalid password")
        except User.DoesNotExist:
            messages.error(request, "No account found with this email")

    return render(request, 'login.html')

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

def logout_user(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect('index')