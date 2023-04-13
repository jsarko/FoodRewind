# From https://medium.com/backticks-tildes/how-to-dockerize-a-django-application-a42df0cb0a99

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.9

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /food_rewind

# Copy the current directory contents into the container at /music_service
ADD . /food_rewind/

WORKDIR /food_rewind

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
# RUN chmod -R +x scripts

# ENV PATH="scripts:/py/bin:$PATH"

EXPOSE 8000

RUN chmod +x /food_rewind/entrypoint.sh
ENTRYPOINT ["/food_rewind/entrypoint.sh"]

# This works but shouldnt be using djangos dev server.
# Need to wire up gunicorn
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
