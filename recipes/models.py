from django.db import models
from tinymce.models import HTMLField

from django.utils.text import slugify

# Create your models here.


class Tags(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255, blank=False)
    tags = models.ManyToManyField(Tags)
    recipe = HTMLField()
    notes = models.TextField(blank=True, null=True)
    image = models.URLField()
    recipe_url = models.URLField(blank=True, null=True)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)
