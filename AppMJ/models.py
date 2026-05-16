from django.db import models

class Album(models.Model):
    titulo = models.CharField(max_length=100) 
    anolanzamiento = models.IntegerField()  
    portada = models.CharField(max_length=200) 

    def __str__(self):
        return self.titulo
