from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ContactForm

def get_user_instance(request):
    """
    Fetch the user instance based on the current session.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - User instance or None if not found.
    """
    user_email = request.user.email
    return User.objects.filter(email=user_email).first()