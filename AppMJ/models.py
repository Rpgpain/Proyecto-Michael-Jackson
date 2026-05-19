from django.db import models

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    anio_lanzamiento = models.IntegerField()
    portada_url = models.CharField(max_length=300)   
    spotify_url = models.CharField(max_length=300)   

    def __str__(self):
        return self.titulo
