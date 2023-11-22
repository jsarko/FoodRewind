from django.db import models
from django.utils import timezone
from datetime import datetime
from .consts import CATEGORY_CHOICES

# Create your models here.

def default_grocery_list_name():
    return datetime.strftime(timezone.now(), "%B %d %Y")

class GroceryItem(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    grocery_list = models.ForeignKey('GroceryList', related_name='groceries', on_delete=models.CASCADE)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES, default="UNCATEGORIZED")
    in_bag = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} | {self.grocery_list.name}"

class GroceryList(models.Model):
    name = models.CharField(max_length=100, default=default_grocery_list_name(), unique=True)
    created_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
