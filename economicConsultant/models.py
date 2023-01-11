from django.db import models


class Specialtys(models.TextChoices):
    INVESTIMENTOS = "Investimentos",
    FINANCAS_PESSOAIS = "Finanças Pessoais",
    POUPANCA = "Poupança"


class EconomicConsultant(models.Model):
    name = models.CharField(max_length=200, unique=True)
    specialty = models.CharField(
        max_length=30,
        choices=Specialtys.choices
    )
