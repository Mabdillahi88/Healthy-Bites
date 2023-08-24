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

class ContactMessage(View):
    """Handles the display and processing of the contact form."""
    
    template_name = 'get-in-touch.html'

    def get(self, request, *args, **kwargs):
        """
        Serve the contact form. 
        If the user is authenticated, their email is pre-filled.
        """
        initial_data = {'email': request.user.email} if request.user.is_authenticated else {}
        contact_form = ContactForm(initial=initial_data)