from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import MealOption, Beverage


@admin.register(MealOption)
class MealOptionAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)  

    list_display = ('meal_name', 'meal_category', 'price', 'available')
    search_fields = ('meal_name', 'description')
    list_filter = ('available', 'meal_category')