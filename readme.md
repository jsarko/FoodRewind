### Todo
- User system
- Add Recipe by URL
    - Use beautifulsoup to scrape the recipe url
    - Given the URL of a recipe, attempts to extract the recipe from the `print` option within the site
        - Will pass this html to prepopulate recipe description
    - Will attempt to derive the recipe image from the page as well
    - Display error if unable to parse recipe automatically
- Fix Tags
- Fix search/autocomplete
- Meal plan features
- Add ingredients from recipe to grocery list
- Auto-categorize groceries
    - GPT can do this but will likely be overkill
    - Might be able to leverage the usda api