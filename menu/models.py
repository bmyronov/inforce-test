from authentication.models import User

from django.db import models
from django.utils import timezone


MEAL_TYPES = (
    ('drink', 'drink'),
    ('breacfast', 'breacfast'),
    ('dessert', 'dessert'),
    ('main', 'main'),
    ('soup', 'soup'),
    ('salad', 'salad'),
    ('alcohol', 'alcohol'),
)


class MenuMeal(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    type = models.CharField(max_length=100, choices=MEAL_TYPES)


class Menu(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_serverd = models.DateField(default=timezone.localdate)
    restaurant = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ManyToManyField(MenuMeal)
