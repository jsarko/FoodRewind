# Generated by Django 4.1.5 on 2023-01-30 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_lists', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grocerylist',
            name='groceries',
        ),
        migrations.AddField(
            model_name='groceryitem',
            name='grocery_list',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='groceries', to='grocery_lists.grocerylist'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='grocerylist',
            name='name',
            field=models.CharField(default='January 30 2023', max_length=100, unique=True),
        ),
    ]
