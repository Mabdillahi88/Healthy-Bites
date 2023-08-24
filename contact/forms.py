from django import forms
from crispy_forms.helper import FormHelper
from phonenumber_field.formfields import PhoneNumberField
from .models import MyContact

class ContactForm(forms.ModelForm):
    """
    A form to capture contact details and messages.
    Uses crispy_forms for improved frontend presentation.
    """
