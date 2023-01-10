from django.db import models


class Invoice(models.Model):
    class Meta:
        ordering = ("id",)
    value = models.FloatField()
    closing_date = models.DateField()
    paid = models.BooleanField(default=False)
    due_date = models.DateField()

    card = models.ForeignKey(
        "card.Card",
        on_delete=models.PROTECT,
        related_name="invoices",
    )

    launch = models.ManyToManyField(
        "launch.Launch",
        related_name="invoices",
    )
