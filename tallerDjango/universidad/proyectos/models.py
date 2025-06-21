from django.db import models

# Create your models here.
class Proyecto(models.Model):
    idproyecto = models.AutoField(primary_key=True)
    nomproyecto = models.CharField(max_length=100)
    tiempo = models.TimeField()
    fechainicio = models.DateField()
    fechafin = models.DateField()
    
    def __str__(self):
        return self.nomproyecto
    