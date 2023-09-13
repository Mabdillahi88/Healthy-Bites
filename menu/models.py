from django.db import models


FOOD_CATEGORIES = (
    (0, 'Starters'),
    (1, 'Mains'),
    (2, 'Desserts'),
    (3, 'New')
)

BEVERAGE_CATEGORIES = (
    (0, 'Smoothie Blends'),
    (1, 'Shake Varieties'),
    (2, 'New')
)


class MealOption(models.Model):
    """
    A class for the meal options model, contains
    starters, mains, desserts, and new arrivals.
    """
    meal_id = models.AutoField(primary_key=True)
    meal_name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.FloatField()
    meal_category = models.IntegerField(choices=FOOD_CATEGORIES, default=3)
    available = models.BooleanField(default=False)

    class Meta:
        ordering = ['-meal_category']

    def __str__(self):
        return self.meal_name


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
        choices=BEVERAGE_CATEGORIES, default=2
    )
    available = models.BooleanField(default=False)

    class Meta:
        ordering = ['-available']

    def __str__(self):
        return self.beverage_name
