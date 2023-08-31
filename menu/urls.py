from django.urls import path
from menu import views


urlpatterns = [
    path('food_menu/', views.display_food, name='food_menu'),
    path('smoothies/', views.display_smoothies, name='smoothies'),
    path('milkshakes/', views.display_shakes, name='milkshakes'),
]
