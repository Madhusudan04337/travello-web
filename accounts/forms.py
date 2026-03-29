from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class RegistrationForm(forms.ModelForm):
    """Form for user registration with validation and user creation logic."""

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}),
        min_length=8,
        help_text="Password must be at least 8 characters long."
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'confirm_password'}),
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        """Validate that the email is unique."""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    def clean(self):
        """Validate that passwords match."""
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        """Create and return a new user."""
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # Use email as username
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user


class LoginForm(AuthenticationForm):
    """Custom login form that uses email instead of username."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Replace the username field with email field
        self.fields['username'] = forms.EmailField(
            widget=forms.EmailInput(attrs={'class': 'form-control'}),
            label="Email"
        )

    def clean(self):
        """Authenticate user with email and password."""
        cleaned_data = super().clean()
        email = cleaned_data.get('username')  # username field now contains email
        password = cleaned_data.get('password')

        if email and password:
            # Try to authenticate using email as username
            self.user_cache = self.authenticate_user(email, password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    "Please enter a correct email and password. Note that both fields may be case-sensitive."
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return cleaned_data

    def authenticate_user(self, email, password):
        """Authenticate user using email."""
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            pass
        return None