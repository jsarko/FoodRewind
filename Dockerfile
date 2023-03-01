# From https://medium.com/backticks-tildes/how-to-dockerize-a-django-application-a42df0cb0a99

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.9

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /food_rewind

# Set the working directory to /music_service
WORKDIR /food_rewind

# Copy the current directory contents into the container at /music_service
ADD . /food_rewind/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt