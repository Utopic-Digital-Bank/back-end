from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("InvestmentCdi", "0001_initial"),
        ("account", "0001_initial"),
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
