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
        
        # Customize the form layout using Crispy Forms.
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('phone', css_class='form-group col-md-6 mb-0'),
                Column('requested_date', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'guest_count',
            'table',
            'requested_time',
            Submit('submit', 'Book Now')
        )
        