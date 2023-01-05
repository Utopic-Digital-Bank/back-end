from django.db import models


class Launc(models.Model):

    value = models.DecimalField(max_digits=9, decimal_places=2)
    establishment = models.CharField(max_length=20)
    date_hour = models.DateTimeField
    invoice = models.CharField(max_length=255) #temporário

    # invoice = models.ForeignKey(
    #     "invoices.Invoice",
    #     on_delete=models.CASCADE,
    #     related_name="launch",
    # )

    def __repr__(self) -> str:
        return f"<[{self.id}] {self.establishment} - {self.value} - {self.date_hour} - {self.invoice}>"
