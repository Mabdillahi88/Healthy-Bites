from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from .models import MyContact


# Registering the MyContact model with Django Admin
@admin.register(MyContact)
class ContactAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = (
        'message_id',
        'user',
        'name',
        'message',
        'phone',
        'created_date'
    )

    # Fields that can be searched in the admin view
    search_fields = ['name', 'email', 'phone']

    # Fields that can be used to filter results in the admin view
    list_filter = (
        'user',
        'name',
        'email',
        'phone',
        ('created_date', DateRangeFilter),
    )
