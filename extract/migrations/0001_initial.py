from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Extract",
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
                (
                    "valueOperation",
                    models.DecimalField(decimal_places=2, max_digits=17),
                ),
                (
                    "previous_balance",
                    models.DecimalField(decimal_places=2, max_digits=17),
                ),
                (
                    "current_balance",
                    models.DecimalField(decimal_places=2, max_digits=17),
                ),
                (
                    "operation",
                    models.CharField(
                        choices=[
                            ("pix", "Pix"),
                            ("transferência", "Transferência"),
                            ("saque", "Saque"),
                            ("pagamento", "Pagamento"),
                            ("depósito", "Depósito"),
                        ],
                        max_length=13,
                    ),
                ),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="extract",
                        to="account.account",
                    ),
                ),
            ],
        ),
    ]
