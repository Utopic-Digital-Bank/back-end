# Generated by Django 4.1.5 on 2023-01-10 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("account", "0001_initial"),
        ("InvestmentCdi", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="investmentcdi",
            name="account",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="investmentsCdi",
                to="account.account",
            ),
        ),
    ]
