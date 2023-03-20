from django import forms
from tinymce.widgets import TinyMCE

class RecipeForm(forms.Form):
    name = forms.CharField(required=True)
    tags = forms.CharField(
        required=False,
        help_text="Separate each tag with a comma."
    )
    recipe_url = forms.URLField(
        required=False, 
        help_text="Url of a recipe on a website."
    )
    recipes = forms.CharField(
        required=False, 
        help_text="Type out a recipe", 
        widget=TinyMCE(attrs={'cols': 30, 'rows': 10}),
        label="Typed Recipe"
    )
    notes = forms.CharField(
        help_text="Add notes to the recipe.", required=False)
    image = forms.URLField(required=False)
