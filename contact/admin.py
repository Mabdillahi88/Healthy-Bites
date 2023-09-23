from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from .models import MyContact

# Registering the MyContact model with Django Admin
@admin.register(MyContact)
class ContactAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = (
        'message_id',  # Display the message ID
        'user',  # Display the user who sent the message
        'name',  # Display the sender's name
        'message',  # Display the message content
        'phone',  # Display the sender's phone number
        'created_date'  # Display the creation date of the message
    )

    # Fields that can be searched in the admin view
    search_fields = ['name', 'email', 'phone']  # Enable searching by name, email, and phone

    # Fields that can be used to filter results in the admin view
    list_filter = (
        'user',  # Filter by user who sent the message
        'name',  # Filter by sender's name
        'email',  # Filter by sender's email
        'phone',  # Filter by sender's phone number
        ('created_date', DateRangeFilter),  # Filter by creation date using a date range
    )
