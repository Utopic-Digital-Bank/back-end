# Generated by Django 4.1.5 on 2023-01-11 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("economicConsultant", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="economicconsultant",
            name="name",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]