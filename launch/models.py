from django.db import models


class ParcelNumber(models.IntegerChoices):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    ELEVEN = 11
    TWELVE = 12


class Launch(models.Model):

    value = models.DecimalField(max_digits=9, decimal_places=2)
    establishment = models.CharField(max_length=20)
    parcel = models.CharField(
        max_length=2,
        choices=ParcelNumber.choices,
    )
    date_hour = models.DateTimeField(auto_now_add=True)

    def __repr__(self) -> str:
        return f"<[{self.id}] {self.establishment} - {self.value} - {self.date_hour} - {self.invoice}>"
