

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="account",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
