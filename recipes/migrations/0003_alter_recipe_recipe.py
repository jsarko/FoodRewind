# Generated by Django 4.1.5 on 2023-11-22 18:34

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_slug_alter_recipe_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
