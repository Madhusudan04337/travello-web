from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
import uuid
from django.core.mail import send_mail
from django.conf import settings
from .models import PasswordResetToken
import threading

def send_reset_email(reset_url, email):
    """Runs in background thread — won't block the request"""
    try:
        send_mail(
            subject="Password Reset - Travello",
            message=f"Click the link to reset your password:\n\n{reset_url}\n\nThis link expires in 15 minutes.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=True,  # Don't crash if email fails
        )
    except Exception as e:
        print(f"Email error: {e}")

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()

        try:
            user = User.objects.get(email=email)
            PasswordResetToken.objects.filter(user=user).delete()
            token_obj = PasswordResetToken.objects.create(user=user)

            reset_url = f"{settings.SITE_URL}/accounts/login/?form=reset&token={token_obj.token}"

            # Send email in background — won't block gunicorn
            thread = threading.Thread(
                target=send_reset_email,
                args=(reset_url, email)
            )
            thread.daemon = True
            thread.start()

        except User.DoesNotExist:
            pass

        # Redirect immediately — don't wait for email
        messages.success(request, "If this email exists, a reset link has been sent.")
        return redirect('login')

    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        form_data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
        }

        # Validate all required fields including first_name
        if not all([first_name, email, password]):
            messages.error(request, "Please fill in all required fields.")
            return render(request, 'register.html', {'form_data': form_data})

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register.html', {'form_data': form_data})

        # Strong password check
        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters.")
            return render(request, 'register.html', {'form_data': form_data})

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'register.html', {'form_data': form_data})

        try:
            # Generate unique username to avoid collision
            unique_username = f"{first_name.lower()}_{uuid.uuid4().hex[:6]}"

            user = User.objects.create_user(
                username=unique_username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )

            messages.success(request, 'Account created! You can now log in.')
            return redirect('login')

        except Exception as e:
            messages.error(request, "An error occurred during registration. Please try again.")
            return render(request, 'register.html', {'form_data': form_data})

    return render(request, 'register.html')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        if not email or not password:
            messages.error(request, "Please fill in all fields.")
            return render(request, 'login.html', {'next': request.GET.get('next', '')})

        try:
            user_obj = User.objects.get(email=email)

            # Use authenticate() instead of check_password directly
            user = authenticate(request, username=user_obj.username, password=password)

            if user is not None:
                login(request, user)
                name = user.first_name if user.first_name else "Traveler"
                messages.success(request, f"Welcome back, {name}!")

                # Check both GET and POST for next_url
                next_url = request.POST.get('next') or request.GET.get('next')
                if next_url and next_url.startswith('/'):  # ✅ Prevent open redirect
                    return redirect(next_url)
                return redirect('index')
            else:
                messages.error(request, "Invalid password.")

        except User.DoesNotExist:
            messages.error(request, "No account found with this email.")

    # Pass next to template so hidden field carries it through POST
    return render(request, 'login.html', {'next': request.GET.get('next', '')})

@never_cache
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('index')

@never_cache  # Prevents back button restoring after logout
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')
