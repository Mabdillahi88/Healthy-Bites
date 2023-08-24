from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

class MyContact(models.Model):
    """
    Represents a contact entry with associated user details and message.
    """
    
    # Unique identifier for the contact
    message_id = models.AutoField(primary_key=True)
    