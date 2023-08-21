from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from datetime import datetime
from phonenumber_field.formfields import PhoneNumberField
from .models import Booking

# This form is used for users to make a booking at our restaurant.
class BookingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        