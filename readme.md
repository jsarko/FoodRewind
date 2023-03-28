### Todo
##### Done
- ~~User system~~
##### Priority
- ~~Persist database~~
- Migrate data to newer tables
- ~~Clicking on Chevron/Grocery Category does not activate accordian.~~
- Meal plan features
- Add ingredients from recipe to grocery list
- Soft delete grocery lists or way to archive
- Food we want to make/places we want to eat in the future
##### Everything Else
- Add Recipe by URL
    - Use beautifulsoup to scrape the recipe url
    - Given the URL of a recipe, attempts to extract the recipe from the `print` option within the site
        - Will pass this html to prepopulate recipe description
    - Will attempt to derive the recipe image from the page as well
    - Display error if unable to parse recipe automatically
- Fix Tags
- Fix search/autocomplete
- Auto-categorize groceries
    - GPT can do this but will likely be overkill
    - Might be able to leverage the usda api
- Split recipe descirption into ingredients w/ measurements and preparation w/ steps
    - Serving size
- Print Button
- Investigate how others apps handle meal planning and recipe input