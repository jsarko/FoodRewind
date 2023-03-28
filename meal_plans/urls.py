from django.urls import path
from meal_plans.views import MealPlanListView, MealPlanCreateView

app_name = 'meal_plan'
urlpatterns = [
    path('', MealPlanListView.as_view(), name='list'),
    path('add', MealPlanCreateView.as_view(), name='create'),
]
