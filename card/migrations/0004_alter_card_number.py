# Generated by Django 4.1.5 on 2023-01-09 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("card", "0003_alter_card_due_card"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card",
            name="number",
            field=models.CharField(max_length=128),
        ),
    ]