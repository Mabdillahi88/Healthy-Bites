from django.shortcuts import render
from .models import MealOption, Beverage

def display_food(request):
    """
    a view to display the food menu
    """
    meal_items = MealOption.objects.all()
    return render(request, 'food_menu.html', {'food_items': meal_items})