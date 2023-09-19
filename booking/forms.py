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
                Column(
                    'requested_date',
                    css_class='form-group col-md-6 mb-0'
                ),
                css_class='form-row'
            ),
            'guest_count',
            'table',
            'requested_time',
            Submit('submit', 'Book Now')
        )

        # Set minimum date for date picker
        min_date = datetime.now().date()
        self.fields['requested_date'].widget.attrs['min'] = min_date

        # Additional field attributes for styling and functionality.
        fields_attrs = {
            'name': 'custom-input',
            'email': 'custom-input',
            'phone': 'custom-input-phone',
            'requested_date': 'custom-date-picker'
        }
        for field, css_class in fields_attrs.items():
            self.fields[field].widget.attrs['class'] = css_class

    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Full Name'}),
        help_text="Please provide your name for the booking."
    )
    phone = PhoneNumberField(
        widget=forms.TextInput(attrs={'placeholder': '+44 1234 567890'}),
        help_text="Provide your phone number, including the country code (+44 for UK)."
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'your-email@example.com'}),
        help_text="We'll send a booking confirmation to the provided email."
    )
    requested_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="Select the date for your booking."
    )

    class Meta:
        model = Booking
        fields = (
            'name',
            'email',
            'phone',
            'guest_count',
            'table',
            'requested_date',
            'requested_time'
        )
