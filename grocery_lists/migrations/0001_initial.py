# Generated by Django 4.1.5 on 2023-01-30 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('in_bag', models.BooleanField(default=False)),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GroceryList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='January 30 2023', max_length=100)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('groceries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery_lists.groceryitem')),
            ],
        ),
    ]
