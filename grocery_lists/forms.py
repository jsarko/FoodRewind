from django.forms import ModelForm, inlineformset_factory, HiddenInput
from .models import GroceryList, GroceryItem

class GroceryListForm(ModelForm):
    class Meta:
        model = GroceryList
        exclude = ['created_on']
        
class GroceryItemForm(ModelForm):
    class Meta:
        model = GroceryItem
        fields = ["is_favorite", 'name', 'in_bag', ]
        widgets = {
            # 'is_favorite': HiddenInput(),
            'in_bag': HiddenInput()
        }
        
GroceryListFormset = inlineformset_factory(GroceryList, GroceryItem,
                                            form=GroceryItemForm, extra=1)