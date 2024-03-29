# Generated by Django 4.1.4 on 2023-01-20 17:27

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('recipe', tinymce.models.HTMLField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('image', models.URLField()),
                ('recipe_url', models.URLField(blank=True, null=True)),
                ('tags', models.ManyToManyField(to='recipes.tags')),
            ],
        ),
    ]
