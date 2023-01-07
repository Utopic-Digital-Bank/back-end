from django.db import models


class Launch(models.Model):

    value = models.DecimalField(max_digits=9, decimal_places=2)
    establishment = models.CharField(max_length=20)
    date_hour = models.DateTimeField
    

    def __repr__(self) -> str:
        return f"<[{self.id}] {self.establishment} - {self.value} - {self.date_hour} - {self.invoice}>"
