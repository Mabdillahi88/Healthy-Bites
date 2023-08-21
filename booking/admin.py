from django.contrib import admin, messages
from rangefilter.filters import DateRangeFilter
from .models import Table, Booking

# Admin configuration for managing tables in the restaurant.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """
    Admin interface for managing tables. Allows for easy viewing of table details
    and searching based on table names.
    """
    # Fields to display in the list view, changing the order for distinctiveness
    list_display = ('name', 'id', 'max_seats')
    
    # Fields that can be used for search in the admin panel
    search_fields = ('name', 'id')

    # Fields that can be used to filter the displayed list, added 'id' for filtering
    list_filter = ('id', 'max_seats')

    # Default ordering based on maximum seats
    ordering = ('max_seats', 'name')

# Admin configuration for managing bookings made by customers.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):