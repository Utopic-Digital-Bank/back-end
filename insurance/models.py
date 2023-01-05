from django.db import models


class Insurance(models.Model):
    name = models.CharField(50),
    tuition = models.DecimalField(max_digits=17, decimal_places=2)
    is_active = models.BooleanField(default=True)
