from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from django.db import transaction

from .models import GroceryList, GroceryItem
from .forms import GroceryListForm, GroceryListFormset
# Create your views here.
class ListGroceryListView(ListView):
    model = GroceryList
    
class CreateGroceryListView(CreateView):
    model = GroceryList
    fields = ["name", ]
    success_url = reverse_lazy('groceries:list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['groceries'] = GroceryListFormset(self.request.POST)
        else:
            data['groceries'] = GroceryListFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        groceries = context['groceries']
        with transaction.atomic():
            self.object = form.save()

            if groceries.is_valid():
                groceries.instance = self.object
                groceries.save()
        return super().form_valid(form)
class DetailGroceryListView(DetailView):
    model = GroceryList