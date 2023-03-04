#!/bin/sh
set -e

gunicorn -b :8000 --chdir /FoodRewind FoodRewind.wsgi:application