from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.db import transaction
from django.http import HttpResponseBadRequest, HttpResponse, JsonResponse

from .models import GroceryList, GroceryItem
from .forms import GroceryListForm, GroceryListFormset
# Create your views here.


class ListGroceryListView(ListView):
    model = GroceryList
    paginate_by = 10
    ordering = ['-created_on']


@login_required
class DeleteGroceryListView(DeleteView):
    model = GroceryList
    success_url = reverse_lazy('groceries:list')


@login_required
class CreateGroceryListView(CreateView):
    model = GroceryList
    fields = ["name", ]
    success_url = reverse_lazy('groceries:list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['groceries'] = GroceryListFormset(self.request.POST or None)
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


@login_required
class UpdateGroceryListView(UpdateView):
    model = GroceryList
    fields = ["name", ]
    success_url = reverse_lazy('groceries:list')

    # Abstract logic to a custom mixin for create and update to reduce duplicate code
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['groceries'] = GroceryListFormset(
            self.request.POST or None, instance=self.object)
        return data

    def form_valid(self, form):
        # TODO: Verify null fields arent saved
        context = self.get_context_data()
        groceries = context['groceries']
        with transaction.atomic():
            self.object = form.save()

            if groceries.is_valid():
                groceries.instance = self.object
                groceries.save()
        return super().form_valid(form)


@login_required
def addToBag(request, pk):
    if request.method == "POST":
        item_id = request.POST.get('itemId')
        in_bag = True if request.POST.get('inBag').lower() == "true" else False
        GroceryItem.objects.filter(pk=item_id).update(in_bag=in_bag)
        items_in_bag = GroceryItem.objects.filter(
            grocery_list__pk=pk, in_bag=True)
        return JsonResponse(list(items_in_bag.values()), safe=False)
    else:
        return HttpResponseBadRequest()


@login_required
def addItemtoList(request):
    if request.method == "POST":
        itemName = request.POST.get('itemName')
        category = request.POST.get('category')
        listID = request.POST.get('listID')
        if (not itemName or not category or not listID):
            return HttpResponseBadRequest()
        gl = GroceryList.objects.get(pk=listID)
        obj = gl.groceries.create(
            name=itemName,
            category=category
        )
        return JsonResponse({"id": obj.pk})
    else:
        return HttpResponseBadRequest()
