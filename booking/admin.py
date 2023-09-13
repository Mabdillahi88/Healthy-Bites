from django.contrib import admin, messages
from rangefilter.filters import DateRangeFilter
from .models import Table, Booking


# Admin configuration for managing tables in the restaurant.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """
    Admin interface for managing tables. Allows for easy viewing 
    of table details and searching based on table names.
    """
    # Fields to display in the list view
    list_display = ('name', 'id', 'max_seats')
    
    # Fields that can be used for search in the admin panel
    search_fields = ('name', 'id')

    # Fields that can be used to filter the displayed list
    list_filter = ('id', 'max_seats')

    # Default ordering based on maximum seats
    ordering = ('max_seats', 'name')


# Admin configuration for managing bookings made by customers.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin interface for managing customer bookings. Provides functionalities
    like searching, filtering, and confirming bookings.
    """
    # Fields to display in the list view
    list_display = (
        'user', 'name', 'phone', 'guest_count', 'status', 'table',
        'requested_date', 'requested_time', 'created_date', 'id'
    )

    # Fields that can be used for search
    search_fields = ['name', 'email', 'phone', 'user']

    # Fields that can be used to filter the displayed list
    list_filter = (
        'status', 'user', 'name', 'email', 'phone', 'guest_count', 'table',
        ('requested_date', DateRangeFilter), 'requested_time', 'created_date'
    )

    # Actions available in the admin panel
    actions = ['confirm_bookings']

    def confirm_bookings(self, request, queryset):
        # A simple permission check, can be enhanced
        if not request.user.has_perm('app.change_booking'):
            messages.error(request, 'You do not have permission to change bookings.')
            return
        queryset.update(status='Booking Confirmed')
    confirm_bookings.short_description = "Confirm selected bookings"
