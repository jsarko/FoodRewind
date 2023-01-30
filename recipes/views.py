from django.shortcuts import render, reverse
from .models import Dish, Tags
from .forms import AddDishForm
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    food = Dish.objects.all()
    tags = Tags.objects.all().order_by("name")
    context = {
        "food": food,
        "tags": tags
    }

    return render(request, 'food_rewind/index.html', context)


def details(request, dish_name):
    dish = Dish.objects.get(name=dish_name)
    context = {
        'dish': dish
    }
    return render(request, 'food_rewind/details.html', context)


def add_dish(request):
    msg = request.GET.get("msg")
    if request.method == 'POST':
        form = AddDishForm(request.POST)

        if form.is_valid():
            # Process
            try:
                raw_tags = form.cleaned_data['tags'].split(',')
                tags = [t.strip() for t in raw_tags]

                d = Dish(
                    name=form.cleaned_data['dish_name'],
                    recipe=form.cleaned_data['recipes'],
                    image=form.cleaned_data['image'],
                    notes=form.cleaned_data['notes']
                )
                # Save separately to assign the object to "d"
                # Otherwise, "d" will return nothing.
                d.save()
            except Exception as e:
                print("Failed on Dish")
                print(e)
            try:
                print(f"Tags: {tags}")
                for tag in tags:
                    t, created = Tags.objects.get_or_create(
                        name=tag
                    )
                    print(f"Created: {tag} - {created}")
                    d.tags.add(t)
            except Exception as e:
                print("Failed on Tags")
                print(e)
            print("Dish added successfully")
            msg = "success"
            return HttpResponseRedirect(reverse('food:add_dish') + f"?msg={msg}")
    else:
        form = AddDishForm()
    context = {
        "form": form,
        "msg": msg
    }

    return render(request, 'food_rewind/add_dish.html', context)
