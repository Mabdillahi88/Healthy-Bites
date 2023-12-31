from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ContactForm


# Utility function to fetch the user instance based on the current session
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


# View class to handle the contact form display and processing
class ContactMessage(View):
    """Handles the display and processing of the contact form."""

    template_name = 'get-in-touch.html'

    def get(self, request, *args, **kwargs):
        """
        Serve the contact form.
        If the user is authenticated, their email is pre-filled.
        """
        initial_data = {'email': request.user.email} if request.user.is_authenticated else {}   # noqa
        contact_form = ContactForm(initial=initial_data)

        return render(
            request,
            self.template_name,
            {'contact_form': contact_form}
        )

    def post(self, request):
        """
        Process the contact form submission.
        If the form is valid, save the contact and display a success message.
        """
        form = ContactForm(data=request.POST)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = get_user_instance(request)
            contact.save()

            messages.success(request, "Message has been sent")
            return render(request, 'confirmation.html')

        return render(
            request,
            self.template_name,
            {'contact_form': form}
        )
