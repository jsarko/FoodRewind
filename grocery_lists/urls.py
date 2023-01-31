from django.urls import path
from . import views

app_name = 'groceries'
urlpatterns = [
    path('', views.ListGroceryListView.as_view(), name='list'),
    path('<int:pk>', views.DetailGroceryListView.as_view(), name="detail"),
    path('<int:pk>/update', views.UpdateGroceryListView.as_view(template_name="grocery_lists/grocerylist_update.html"), name="update"),
    path('create', views.CreateGroceryListView.as_view(template_name="grocery_lists/grocerylist_create.html"), name='create'),
]
