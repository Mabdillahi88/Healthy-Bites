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

class Table(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='New Table', unique=True, help_text="The name of the table.")
    max_seats = models.PositiveIntegerField(default=2, help_text="Max seating capacity of the table.")

    class Meta:
        # Order tables by their seating capacity (descending).
        ordering = ['-max_seats']

    def __str__(self):
        return self.name
