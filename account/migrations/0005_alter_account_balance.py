# Generated by Django 4.1.5 on 2023-01-09 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0004_account_insurance_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="balance",
            field=models.FloatField(default=0.0),
        ),
    ]
