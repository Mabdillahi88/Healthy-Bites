from django.shortcuts import render
from .models import MealOption, Beverage

def display_food(request):
    """
    a view to display the food menu
    """
    meal_items = MealOption.objects.all()
    return render(request, 'food_menu.html', {'food_items': meal_items})

def display_smoothies(request):
    """
    a view to showcase the smoothie blends menu
    """
    blends_list = Beverage.objects.filter(beverage_category=0)
    return render(request, 'smoothies.html', {'blends_list': blends_list})

def display_shakes(request):
    """
    a view to showcase the shake varieties menu
    """
    shake_list = Beverage.objects.filter(beverage_category=1)
    return render(request, 'milkshakes.html', {'shake_list': shake_list})
