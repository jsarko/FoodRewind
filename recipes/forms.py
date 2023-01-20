from django import forms
from tinymce.widgets import TinyMCE

class RecipeForm(forms.Form):
    name = forms.CharField(required=True)
    tags = forms.CharField(
        required=True, help_text="Separate each tag with a comma.")
    recipe_url = forms.URLField(required=False, help_text="Url of a recipe on a website.")
    recipes = forms.CharField(
        required=True, help_text="Enter a recipe or a link to a recipe.", widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    notes = forms.CharField(
        help_text="Add notes to the recipe.", required=False)
    image = forms.URLField(required=True)
