# Generated by Django 4.1.5 on 2023-01-06 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("launch", "0002_launch_delete_launc"),
    ]

    operations = [
        migrations.AddField(
            model_name="launch",
            name="date_hour",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="launch",
            name="parcel",
            field=models.CharField(
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
                default=1,
                max_length=2,
            ),
        ),
    ]