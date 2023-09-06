from django.db import models
from django.contrib.auth.models import User

from .consts import MEAL_TYPE_CHOICES
# Create your models here.

class MealPlan(models.Model):
    user = models.ForeignKey(
        to=User, 
        on_delete=models.CASCADE, 
        related_name="meal_plan"
    )
    name = models.CharField(max_length=255)
    meal_type = models.CharField(max_length=255, choices=MEAL_TYPE_CHOICES, default="DINNER")
    meal_date = models.DateField()
    recipe_link = models.URLField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

class Wishlist(models.Model):
    user = models.ForeignKey(
        to=User, 
        on_delete=models.CASCADE, 
        related_name="wishlist"
    )
    name = models.CharField(max_length=255)
    recipe_link = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)