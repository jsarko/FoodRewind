from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_dish', views.add_dish, name='add_dish'),
    path('<dish_name>', views.details, name='details'),
]
