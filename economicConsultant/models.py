from django.db import models


class EconomicConsultant(models.Model):
    name = models.CharField(50)
    specialty = models.CharField(50)
