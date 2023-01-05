from django.db import models


class Account(models.Model):
    balance = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)

    user_id = models.OneToOneField(
        "users.User",
        on_delete=models.PROTECT,
        related_name="account",
    )
    # insurance_id = models.ManyToManyField(
    #     "insurance.Insurance",
    #     on_delete=models.CASCADE,
    #     related_name="account",
    #     blank=True,
    #     null=True,
    # )
    economic_consultance_id = models.ForeignKey(
        "economicConsultant.EconomicConsultant",
        on_delete=models.PROTECT,
        related_name="account",
        blank=True,
        null=True,
        )
