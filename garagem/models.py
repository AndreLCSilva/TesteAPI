from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from pessoa.models import NewUser

class Garagem(models.Model):
    garage_name = models.CharField(max_length=20, blank=True)
    user_name = models.ForeignKey(NewUser, related_name='user_name', on_delete=models.CASCADE)

    def __str__(self):
       return self.garage_name


class Vehicle(models.Model):
    TYPES = (
            ('C', 'Carro'),
            ('M', 'Moto'),
    )
    type = models.CharField(choices=TYPES, max_length=1)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    garage = models.ForeignKey(Garagem, related_name='garage', on_delete=models.CASCADE)

    def __str__(self):
        return self.model