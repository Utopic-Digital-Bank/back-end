# Generated by Django 4.1.5 on 2023-01-09 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_remove_user_first_name_remove_user_last_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="monthly_income",
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]