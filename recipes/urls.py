from django.urls import path
from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.recipe_list, name='list'),
    path('recipes/add_recipe', views.add_recipe, name='create'),
    path('recipes/<int:pk>/', views.recipe_details, name='details'),
]
