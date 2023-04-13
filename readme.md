### Todo
##### Done
- ~~User system~~
- ~~Clicking on Chevron/Grocery Category does not activate accordian.~~
- ~~Meal plan features~~
- ~~Persist database~~
- ~~Admin Panel~~
##### Priority
- Migrate data to newer tables
- Food we want to make/places we want to eat in the future

##### Bugs
- Static files dont work when debug set to False
- Fix Tags
- Fix search/autocomplete

##### Features
- Wire up Gunicorn
- Error pages
- Soft delete grocery lists or way to archive
- Add ingredients from recipe to grocery list
- Add Recipe by URL
    - Use beautifulsoup to scrape the recipe url
    - Given the URL of a recipe, attempts to extract the recipe from the `print` option within the site
        - Will pass this html to prepopulate recipe description
    - Will attempt to derive the recipe image from the page as well
    - Display error if unable to parse recipe automatically
- Auto-categorize groceries
    - GPT can do this but will likely be overkill
    - Might be able to leverage the usda api
- Split recipe descirption into ingredients w/ measurements and preparation w/ steps
    - Serving size
- Print Button
- Investigate how others apps handle meal planning and recipe input


## Building and Deploying with Docker
- `docker-compose up --build` or `docker-compose build`
- `aws lightsail push-container-image --service-name container-service-1 --label food-rewind-for-real --image foodrewind_web:latest`
- Deploy in lightsail