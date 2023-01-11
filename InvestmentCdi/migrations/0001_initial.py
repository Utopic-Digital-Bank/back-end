from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="InvestmentCdi",
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
                ("initial_value", models.DecimalField(decimal_places=2, max_digits=17)),
                (
                    "current_value",
                    models.DecimalField(decimal_places=2, max_digits=17, null=True),
                ),
                (
                    "yield_value",
                    models.DecimalField(decimal_places=2, max_digits=17, null=True),
                ),
                ("creation_date", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
