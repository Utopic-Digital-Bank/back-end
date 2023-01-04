from django.db import models


class InvestmentCdi(models.Model):
    initial_value = models.DecimalField(max_digits=17, decimal_places=2)
    current_value = models.DecimalField(max_digits=17, decimal_places=2)
    yield_value = models.DecimalField(max_digits=17, decimal_places=2)
    creation_date = models.DateField(auto_now_add=True)
    account = models.ForeignKey(
        "account.account", related_name="investmentsCdi", on_delete=models.PROTECT)
