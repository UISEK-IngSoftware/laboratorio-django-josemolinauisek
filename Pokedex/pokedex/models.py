from django.db import models

class Pokemon(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    peso = models.FloatField()
    altura = models.FloatField()
    descripcion = models.TextField()
    imagen = models.CharField(max_length=100)  # Ruta relativa dentro de /static/

    def __str__(self):
        return self.nombre
