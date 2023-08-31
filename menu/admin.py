from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import MealOption, Beverage


@admin.register(MealOption)
class MealOptionAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)  