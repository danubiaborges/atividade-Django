from django.db import models

class avaliarPassageiro(models.Model):
    idCorrida = models.IntegerField()
    nomePass = models.CharField(max_length=255)
    nota = models.IntegerField()
    comentario = models.TextField()