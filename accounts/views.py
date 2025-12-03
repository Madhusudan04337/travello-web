from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

# ... other imports

def register(req):
    if req.method == 'POST':
        # Retrieve form data
        username = req.POST['username']
        email = req.POST['email']
        password1 = req.POST['password1']
        password2 = req.POST['password2']

        # 1. Validation for password match and field presence (which you likely have)
        if password1 != password2:
            messages.error(req, 'Passwords do not match')
            return redirect('register')
        
        # 2. Add the check for existing username
        if User.objects.filter(username=username).exists():
            messages.error(req, 'Username already exists. Please choose a different one.')
            return redirect('register')

        # 3. Create the user only if validation passes
        if not User.objects.filter(username=username).exists():
            # The line that caused the error is here:
            user = User.objects.create_user(username=username, password=password1, email=email)
            user.save()
            
            # Optional: Add a success message
            messages.success(req, 'Registration successful. You can now log in.')
             # Or wherever you want to redirect after success

    return render(req, 'register.html')