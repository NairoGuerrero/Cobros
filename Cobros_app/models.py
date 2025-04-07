from django.db import models

class Cliente(models.Model):
    CIUDADES = [
        ('La Dorada', 'La Dorada'),
        ('Honda', 'Honda'),
        ('Mariquita', 'Mariquita'),
    ]

    PUNTUACIONES = [
        ('bueno', 'Bueno'),
        ('regular', 'Regular'),
        ('malo', 'Malo'),
    ]

    nombre = models.CharField(max_length=100)
    alias = models.CharField(max_length=50, blank=True, null=True)
    ciudad = models.CharField(max_length=20, choices=CIUDADES)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    puntuacion = models.CharField(max_length=10, choices=PUNTUACIONES, default='bueno')
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
