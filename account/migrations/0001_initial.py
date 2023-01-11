

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("economicConsultant", "0001_initial"),
        ("insurance", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
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
                ("balance", models.FloatField(default=0.0)),
                ("created_at", models.DateTimeField(auto_now=True)),
                (
                    "economic_consultance_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="account",
                        to="economicConsultant.economicconsultant",
                    ),
                ),
                (
                    "insurance_id",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="account",
                        to="insurance.insurance",
                    ),
                ),
            ],
        ),
    ]
