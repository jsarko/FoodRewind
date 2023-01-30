from django.forms import ModelForm, inlineformset_factory
from .models import GroceryList, GroceryItem

class GroceryListForm(ModelForm):
    class Meta:
        model = GroceryList
        exclude = ['created_on']
        
class GroceryItemForm(ModelForm):
    class Meta:
        model = GroceryItem
        fields = ['name', 'in_bag', "is_favorite"]
        
GroceryListFormset = inlineformset_factory(GroceryList, GroceryItem,
                                            form=GroceryItemForm)