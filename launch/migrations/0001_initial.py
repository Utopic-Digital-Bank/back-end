

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Launch",
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
                ("value", models.DecimalField(decimal_places=2, max_digits=9)),
                ("establishment", models.CharField(max_length=20)),
                (
                    "parcel",
                    models.CharField(
                        choices=[
                            (1, "One"),
                            (2, "Two"),
                            (3, "Three"),
                            (4, "Four"),
                            (5, "Five"),
                            (6, "Six"),
                            (7, "Seven"),
                            (8, "Eight"),
                            (9, "Nine"),
                            (10, "Ten"),
                            (11, "Eleven"),
                            (12, "Twelve"),
                        ],
                        max_length=2,
                    ),
                ),
                ("date_hour", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
