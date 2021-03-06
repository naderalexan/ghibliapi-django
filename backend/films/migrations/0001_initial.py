# Generated by Django 3.0.5 on 2020-07-13 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.UUIDField(db_index=True, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name="Film",
            fields=[
                (
                    "id",
                    models.UUIDField(db_index=True, primary_key=True, serialize=False),
                ),
                ("title", models.CharField(max_length=128)),
                (
                    "people",
                    models.ManyToManyField(related_name="films", to="films.Person"),
                ),
            ],
        ),
    ]
