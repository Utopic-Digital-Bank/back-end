from django.db import models


class Account(models.Model):
    balance = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now=True)

    user = models.OneToOneField(
        "users.User",
        on_delete=models.PROTECT,
        related_name="account",
    )
    insurance = models.ManyToManyField(
        "insurance.Insurance",
        related_name="account",
        blank=True,
        null=True,
    )
    economic_consultance = models.ForeignKey(
        "economicConsultant.EconomicConsultant",
        on_delete=models.PROTECT,
        related_name="account",
        blank=True,
        null=True,
    )
