# Generated by Django 4.1.5 on 2023-04-11 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_lists', '0012_alter_grocerylist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocerylist',
            name='name',
            field=models.CharField(default='April 11 2023', max_length=100, unique=True),
        ),
    ]
