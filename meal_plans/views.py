from django.views.generic import ListView, CreateView
from django.db import transaction
from django.utils import timezone

from meal_plans.models import MealPlan, Wishlist
from meal_plans.forms import MealPlanForm, WishlistForm

# Create your views here.
class MealPlanListView(ListView):
    model = MealPlan
    paginate_by = 10
    
    def get_queryset(self):
        queryset = MealPlan.objects.filter(
            user=self.request.user,
            meal_date__gte=timezone.now()
        ).order_by("meal_date")
        return queryset

class MealPlanCreateView(CreateView):
    model = MealPlan
    form_class = MealPlanForm
    success_url = "/meals/add"
    
    def form_valid(self, form):
        user = self.request.user 
        with transaction.atomic():
            self.object = form.save(commit=False)
            self.object.user_id = user.pk
            
        return super().form_valid(form)

class WishlistListCreateView(CreateView):
    model = Wishlist
    form_class = WishlistForm
    template_name = "meal_plans/wishlist.html"
    success_url = "/meals/wishlist"

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Wishlist.objects.order_by('created_on')
        return super(WishlistListCreateView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        user = self.request.user 
        with transaction.atomic():
            self.object = form.save(commit=False)
            self.object.user_id = user.pk
            
        return super().form_valid(form)