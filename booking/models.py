from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Define available booking time slots from 12:00 to 23:00.
time_slots = tuple(
    (f"{hour:02}:00", f"{hour:02}:00") for hour in range(12, 24)
)

# Define potential statuses for a booking.
statuses = [
    'Waiting',
    'Booked',
    'Declined',
    'Timed Out'
]

status_options = tuple(
    (status.lower(), status) for status in statuses
)


class Table(models.Model):
    """
    Represents a table in the restaurant.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=50, default='New Table', unique=True,
        help_text="The name of the table."
    )
    max_seats = models.PositiveIntegerField(
        default=2, help_text="Max seating capacity of the table."
    )

    class Meta:
        # Order tables by their seating capacity (descending).
        ordering = ['-max_seats']

    def __str__(self):
        return self.name


class Booking(models.Model):
    """
    Represents a customer's booking in the restaurant.
    """
    id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the booking was created."
    )
    requested_date = models.DateField(
        help_text="Desired date for the reservation."
    )
    requested_time = models.CharField(
        max_length=25, choices=time_slots, default='17:00',
        help_text="Desired time for the reservation."
    )
    # Table that's being booked.
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE,
        related_name="reservations", null=True
    )
    # User who made the booking.
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="bookings", null=True
    )
    # Customer details.
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254, default="")
    phone = PhoneNumberField(null=True)

    status = models.CharField(
        max_length=25, choices=status_options, default='waiting'
    )
    guest_choices = (
        (1, "1 Guest"),
        (2, "2 Guests"),
        (3, "3 Guests"),
        (4, "4 Guests"),
        (5, "5 Guests"),
        (6, "6 Guests"),
    )
    guest_count = models.IntegerField(choices=guest_choices, default=2)

    class Meta:
        # Order bookings by requested time.
        # Ensure uniqueness for date, time, and table combination.
        ordering = ['-requested_time']
        unique_together = ('requested_date', 'requested_time', 'table')

    def __str__(self):
        return (
            f"{self.name} on {self.requested_date} "
            f"at {self.requested_time} - {self.status}"
        )
