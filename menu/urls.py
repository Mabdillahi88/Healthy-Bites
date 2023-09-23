from django.urls import path
from menu import views

# URL patterns for menu-related views
urlpatterns = [
    path('food_menu/', views.display_food, name='food_menu'),   # URL for displaying the food menu
    path('smoothies/', views.display_smoothies, name='smoothies'),  # URL for displaying smoothie options
    path('milkshakes/', views.display_shakes, name='milkshakes'),  # URL for displaying milkshake options
]
