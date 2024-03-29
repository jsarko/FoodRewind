# Generated by Django 4.1.5 on 2023-11-22 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_lists', '0017_alter_groceryitem_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='category',
            field=models.CharField(choices=[('UNCATEGORIZED', 'Uncategorized'), ('ALCOHOL', 'Alcohol'), ('BAKERY', 'Bakery'), ('BEAUTY', 'Beauty'), ('BEVERAGE', 'Beverage'), ('CONDIMENT', 'Condiment'), ('DAIRY', 'Dairy'), ('DELI', 'Deli'), ('FROZEN', 'Frozen'), ('PANTRY', 'Pantry'), ('PRODUCE', 'Produce'), ('HOUSEHOLD', 'Household'), ('PET', 'Pet'), ('PROTEIN', 'Protein'), ('SPICE', 'Spice'), ('WELLNESS', 'Wellness')], default='UNCATEGORIZED', max_length=200),
        ),
        migrations.AlterField(
            model_name='grocerylist',
            name='name',
            field=models.CharField(default='November 22 2023', max_length=100, unique=True),
        ),
    ]
