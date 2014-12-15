from django.db import models
from django.utils import timezone

# Create your models here.
class Interesados (models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidoPaterno = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    extension = models.CharField(max_length=10)
    celular = models.CharField(max_length=10)
    insertDate = models.DateTimeField()

    def __str__(self):
    	return (self.nombres + " " + self.apellidoPaterno)

    def interesadosHoy(self):
        return self.insertDate.date() == timezone.now().date()