#!/bin/bash

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
gunicorn FoodRewind.wsgi --bind 0.0.0.0:8000 --forwarded-allow-ips='*' --access-logfile -