from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


time_slots = tuple((f"{hour:02}:00", f"{hour:02}:00") for hour in range(12, 24))


statuses = [
    'Awaiting Confirmation',
    'Booking Confirmed',
    'Booking Rejected',
    'Booking Expired'
]
status_options = tuple((status.lower(), status) for status in statuses)