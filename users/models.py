from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    birthdate = models.DateField()
    cpf = models.CharField(max_length=11)
