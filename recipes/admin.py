from django.contrib import admin
from .models import Recipe, Tags
# Register your models here.

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass