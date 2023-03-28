from django.forms import ModelForm, CharField, TextInput, URLField, URLInput
from .models import MealPlan

class MealPlanForm(ModelForm):
    meal_date = CharField(label='Meal Date',
                    widget=TextInput(
                        attrs={'class': "datepicker", 'placeholder': 'Pick a date'}
                    )
                )
    recipe_link = URLField(label='Recipe Link',
                    required=False,
                    widget=URLInput(
                        attrs={'placeholder': 'Optional...'}
                    )
                )
    class Meta:
        model = MealPlan
        exclude = ['user','created_on']
        
