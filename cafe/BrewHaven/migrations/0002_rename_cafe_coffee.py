# Generated by Django 5.0.2 on 2024-04-23 07:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("BrewHaven", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="cafe",
            new_name="Coffee",
        ),
    ]