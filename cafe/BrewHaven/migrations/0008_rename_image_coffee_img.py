# Generated by Django 5.0.4 on 2024-04-23 09:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("BrewHaven", "0007_alter_coffee_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="coffee",
            old_name="image",
            new_name="img",
        ),
    ]