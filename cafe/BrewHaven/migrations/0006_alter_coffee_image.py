# Generated by Django 5.0.4 on 2024-04-23 09:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("BrewHaven", "0005_alter_coffee_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coffee",
            name="image",
            field=models.ImageField(null=True, upload_to="static/img/coffees/"),
        ),
    ]