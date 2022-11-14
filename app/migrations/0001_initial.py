# Generated by Django 4.1.3 on 2022-11-14 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
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
                ("content", models.TextField()),
                ("datetime", models.DateTimeField(auto_now_add=True)),
                ("deadline", models.DateTimeField(null=True)),
                ("status", models.BooleanField()),
                (
                    "tags",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.tag"
                    ),
                ),
            ],
        ),
    ]
