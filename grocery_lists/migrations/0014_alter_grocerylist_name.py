# Generated by Django 4.1.5 on 2023-04-13 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_lists', '0013_alter_grocerylist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocerylist',
            name='name',
            field=models.CharField(default='April 13 2023', max_length=100, unique=True),
        ),
    ]
