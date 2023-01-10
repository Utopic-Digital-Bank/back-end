# Generated by Django 4.1.5 on 2023-01-10 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EconomicConsultant",
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
                ("name", models.CharField(max_length=200)),
                (
                    "specialty",
                    models.CharField(
                        choices=[
                            ("Investimentos", "Investimentos"),
                            ("Finanças Pessoais", "Financas Pessoais"),
                            ("Poupança", "Poupanca"),
                        ],
                        max_length=30,
                    ),
                ),
            ],
        ),
    ]
