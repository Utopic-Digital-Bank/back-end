from django.db import models


class EconomicConsultant(models.Model):
    name = models.CharField(max_length=200)
    specialty = models.CharField(max_length=50)
