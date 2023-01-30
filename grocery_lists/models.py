from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.

def default_grocery_list_name():
    return datetime.strftime(timezone.now(), "%B %d %Y")

class GroceryItem(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    grocery_list = models.ForeignKey('GroceryList', related_name='groceries', on_delete=models.CASCADE)
    in_bag = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class GroceryList(models.Model):
    name = models.CharField(max_length=100, default=default_grocery_list_name(), unique=True)
    created_on = models.DateTimeField(auto_now=True)
