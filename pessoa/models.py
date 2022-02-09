from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class personData(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    idUser = models.OneToOneField(User, on_delete=CASCADE, primary_key=True)

    class Meta:
        db_table = 'person'

    def __str__(self):
        return self.name
