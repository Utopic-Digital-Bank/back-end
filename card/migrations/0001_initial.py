

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Card",
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
                ("number", models.CharField(max_length=128)),
                ("password", models.CharField(max_length=4)),
                ("cvv", models.CharField(max_length=3)),
                ("balance_invoices", models.FloatField(max_length=17)),
                (
                    "due_date",
                    models.CharField(
                        choices=[
                            ("05", "First Option"),
                            ("15", "Second Option"),
                            ("29", "Third Option"),
                        ],
                        default="05",
                        max_length=8,
                    ),
                ),
                ("due_card", models.CharField(max_length=8)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Debit", "Debit"),
                            ("Credit", "Credit"),
                            ("Múltiplo", "Both"),
                        ],
                        default="Debit",
                        max_length=8,
                    ),
                ),
                ("total_limit", models.FloatField(max_length=17)),
                ("available_limit", models.FloatField(max_length=17)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="card",
                        to="account.account",
                    ),
                ),
            ],
        ),
    ]
