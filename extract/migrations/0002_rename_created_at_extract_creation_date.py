# Generated by Django 4.1.5 on 2023-01-09 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("extract", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="extract",
            old_name="created_at",
            new_name="creation_date",
        ),
    ]