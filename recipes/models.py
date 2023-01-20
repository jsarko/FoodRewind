from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Tags(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    tags = models.ManyToManyField(Tags)
    recipe = HTMLField()
    notes = models.TextField(blank=True, null=True)
    image = models.URLField()
    recipe_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name