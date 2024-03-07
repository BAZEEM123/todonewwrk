# Generated by Django 4.2.7 on 2024-03-06 07:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movieapp", "0002_movie_img"),
    ]

    operations = [
        migrations.CreateModel(
            name="add_update",
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
                ("name", models.CharField(max_length=250)),
                ("desc", models.TextField()),
                ("year", models.IntegerField()),
                ("img", models.ImageField(upload_to="gallery")),
            ],
        ),
    ]
