from django.db import models

# Create your models here.
PLATAFORMA = (
    ('Nintendo Switch', 'Nintendo Switch'),
    ('Xbox', 'Xbox'),
    ('Playstation', 'Playstation'),
    ('PC', 'PC'),
    ('Multiplataforma', 'Multiplataforma'),
    ('No informada', 'No informada')
)

class Lanzamiento (models.Model):
    foto = models.ImageField(upload_to='static/img/lanzamientos')
    nombre = models.CharField(max_length=50)
    plataforma = models.CharField(max_length=50, choices=PLATAFORMA)
    fecha = models.DateField()
    descripcion = models.TextField(max_length=1000)

    def __str__(self):
        return str(self.nombre)
