# Generated by Django 3.2.22 on 2023-10-18 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_meal_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='meal_type',
            field=models.CharField(choices=[('starter', 'starter'), ('main', 'main'), ('dessert', 'dessert'), ('drink', 'drink')], max_length=100),
        ),
    ]
