# Generated by Django 4.1.5 on 2023-03-27 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MealPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('meal_type', models.CharField(choices=[('BREAKFAST', 'Breakfast'), ('LUNCH', 'Lunch'), ('DINNER', 'Dinner')], max_length=255)),
                ('meal_date', models.DateField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='meal_plan', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
