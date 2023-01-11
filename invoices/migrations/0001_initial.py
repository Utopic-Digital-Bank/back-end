

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("launch", "0001_initial"),
        ("card", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Invoice",
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
                ("value", models.FloatField()),
                ("closing_date", models.DateField()),
                ("paid", models.BooleanField(default=False)),
                ("due_date", models.DateField()),
                (
                    "card",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="invoices",
                        to="card.card",
                    ),
                ),
                (
                    "launch",
                    models.ManyToManyField(related_name="invoices", to="launch.launch"),
                ),
            ],
            options={
                "ordering": ("id",),
            },
        ),
    ]
