from django.db import models

# Choices for food categories
FOOD_CATEGORIES = (
    (0, 'Starters'),
    (1, 'Mains'),
    (2, 'Desserts'),
    (3, 'New')
)

# Choices for beverage categories
BEVERAGE_CATEGORIES = (
    (0, 'Smoothie Blends'),
    (1, 'Shake Varieties'),
    (2, 'New')
)

# Model for meal options
class MealOption(models.Model):
    """
    A class for the meal options model, contains
    starters, mains, desserts, and new arrivals.
    """
    meal_id = models.AutoField(primary_key=True)
    meal_name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.FloatField()
    meal_category = models.IntegerField(choices=FOOD_CATEGORIES, default=3)  # Using choices for meal categories
    available = models.BooleanField(default=False)

    class Meta:
        ordering = ['-meal_category']  # Ordering meals by their category

    def __str__(self):
        return self.meal_name

# Model for beverage options
class Beverage(models.Model):
    """
    A class for the beverage options, contains
    smoothie blends, shake varieties, and new beverages.
    """
    beverage_id = models.AutoField(primary_key=True)
    beverage_name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.FloatField()
    beverage_category = models.IntegerField(
        choices=BEVERAGE_CATEGORIES, default=2  # Using choices for beverage categories
    )
    available = models.BooleanField(default=False)

    class Meta:
        ordering = ['-available']  # Ordering beverages by their availability

    def __str__(self):
        return self.beverage_name
