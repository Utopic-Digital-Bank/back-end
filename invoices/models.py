from django.db import models

class Invoice(models.Model):
    class Meta:
        ordering = ("id",)
    value = models.FloatField(max_length=17)
    month = models.CharField(max_length=20)
    paid = models.BooleanField(default=False)
    due_date = models.DateField()

    card = models.ForeignKey(
        "cards.Card",
        on_delete=models.PROTECT,
        related_name="invoices",
    )

    launch = models.ManyToManyField(
        "launchs.Launch",
        related_name="invoices",
    )