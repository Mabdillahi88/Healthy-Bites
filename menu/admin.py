from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import MealOption, Beverage


# Registering the MealOption model with Summernote support
@admin.register(MealOption)
class MealOptionAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

    list_display = (
        'meal_name', 'meal_category', 'price', 'available'
    )

    search_fields = ('meal_name', 'description')

    list_filter = ('available', 'meal_category')


# Registering the Beverage model with Summernote support
@admin.register(Beverage)
class BeverageAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

    list_display = (
        'beverage_name', 'beverage_category', 'price', 'available'
    )

    search_fields = ('beverage_name', 'description')

    list_filter = ('available', 'beverage_category')
