from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import MealOption, Beverage

# Registering the MealOption model with Summernote support
@admin.register(MealOption)
class MealOptionAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)  # Adding Summernote rich text editor to the 'description' field

    list_display = ('meal_name', 'meal_category', 'price', 'available')  # Displayed fields in the admin list view
    search_fields = ('meal_name', 'description')  # Fields that can be searched in the admin view
    list_filter = ('available', 'meal_category')  # Fields that can be used to filter results in the admin view

# Registering the Beverage model with Summernote support
@admin.register(Beverage)
class BeverageAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)  # Adding Summernote rich text editor to the 'description' field

    list_display = ('beverage_name', 'beverage_category', 'price', 'available')  # Displayed fields in the admin list view
    search_fields = ('beverage_name', 'description')  # Fields that can be searched in the admin view
    list_filter = ('available', 'beverage_category')  # Fields that can be used to filter results in the admin view
