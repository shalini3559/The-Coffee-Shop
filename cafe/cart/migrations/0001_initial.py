# Generated by Django 5.0.4 on 2024-05-06 09:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("BrewHaven", "0008_rename_image_coffee_img"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cart_id", models.CharField(blank=True, max_length=255)),
                ("quantity", models.IntegerField(default=1)),
                ("totalprice", models.FloatField(default=0.0)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "coffee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="BrewHaven.coffee",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "cart",
            },
        ),
    ]