from django.shortcuts import render, reverse
from .models import Recipe, Tags
from .forms import RecipeForm
from django.http import HttpResponseRedirect
# Create your views here.


def recipe_list(request):
    food = Recipe.objects.all()
    tags = Tags.objects.all().order_by("name")
    context = {
        "food": food,
        "tags": tags
    }

    return render(request, "recipes/recipe_list.html", context)


def recipe_details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {
        'recipe': recipe
    }
    return render(request, reverse('recipes:details', pk), context)


def add_recipe(request):
    msg = request.GET.get("msg")
    if request.method == 'POST':
        form = RecipeForm(request.POST)

        if form.is_valid():
            # Process
            try:
                raw_tags = form.cleaned_data['tags'].split(',')
                tags = [t.strip() for t in raw_tags]

                r = Recipe(
                    name=form.cleaned_data['name'],
                    recipe=form.cleaned_data['recipes'],
                    image=form.cleaned_data['image'],
                    notes=form.cleaned_data['notes']
                )
                # Save separately to assign the object to "d"
                # Otherwise, "d" will return nothing.
                r.save()
            except Exception as e:
                print("Failed on Recipe")
                print(e)
            try:
                print(f"Tags: {tags}")
                for tag in tags:
                    t, created = Tags.objects.get_or_create(
                        name=tag
                    )
                    print(f"Created: {tag} - {created}")
                    r.tags.add(t)
            except Exception as e:
                print("Failed on Tags")
                print(e)
            print("Recipe added successfully")
            msg = "success"
            return HttpResponseRedirect(reverse('recipes:create') + f"?msg={msg}")
    else:
        form = RecipeForm()
    context = {
        "form": form,
        "msg": msg
    }

    return render(request, 'recipes/add_recipe.html', context)
