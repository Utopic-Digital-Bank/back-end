# Generated by Django 4.1.5 on 2023-01-12 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Insurance",
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
                ("name", models.CharField(max_length=50, unique=True)),
                ("tuition", models.DecimalField(decimal_places=2, max_digits=17)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
    ]
