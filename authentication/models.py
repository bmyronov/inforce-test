from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    restaurant_name = models.CharField(max_length=255)
    is_employee = models.BooleanField(default=False)
    is_restaurant = models.BooleanField(default=False)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    last_vote_time = models.DateField(null=True)
