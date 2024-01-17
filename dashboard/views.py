from django.shortcuts import render
import grocery_lists
from recipes.models import Recipe, Tags
from grocery_lists.models import GroceryList

# Create your views here.
def home(request):
    recipes = Recipe.objects.all()
    tags = Tags.objects.all().order_by("name")
    grocery_lists = GroceryList.objects.all()
    context = {
        "recipes": recipes,
        "tags": tags,
        "grocery_lists": grocery_lists,
    }
    return render(request, 'dashboard/home.html', context=context)