from django.contrib import admin, messages
from rangefilter.filters import DateRangeFilter
from .models import Table, Booking

# Admin configuration for managing tables in the restaurant.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):