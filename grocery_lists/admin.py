from django.contrib import admin
from .models import GroceryItem, GroceryList
# Register your models here.

@admin.register(GroceryItem)
class GroceryItemAdmin(admin.ModelAdmin):
    pass

@admin.register(GroceryList)
class GroceryListAdmin(admin.ModelAdmin):
    pass