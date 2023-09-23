from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

class MyContact(models.Model):
    """
    Represents a contact entry with associated user details and message.
    """
    # Unique identifier for the contact
    message_id = models.AutoField(primary_key=True)

    # Date and time when the contact was created
    created_date = models.DateTimeField(auto_now_add=True)

    # Associated user for the contact
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="contact_thing",
    )

    # Personal details of the contact
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254, default="")
    phone = PhoneNumberField(null=True)

    # Message details
    message = models.TextField()

    class Meta:
        # Sorting contacts by their creation date
        ordering = ['created_date']

    # Return the name when the object is printed or converted to a string
    def __str__(self):
        return f"Contact: {self.name}"
