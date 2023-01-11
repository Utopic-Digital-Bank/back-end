# Generated by Django 4.1.5 on 2023-01-11 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("insurance", "0001_initial"),
        ("account", "0004_alter_account_insurance"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="insurance",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="account", to="insurance.insurance"
            ),
        ),
    ]
