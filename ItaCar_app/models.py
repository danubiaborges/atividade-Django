from distutils.archive_util import make_zipfile
from xml.parsers.expat import model
#biblioteca do django para trabalhar com o banco de dados
from django.db import models
from django.forms import CharField, Field
from django.utils import timezone
import datetime

class avaliacao(models.Model):
    idCorrida = models.IntegerField()
    nomePass = models.CharField(max_length=255)
    nota = models.IntegerField()
    comentario = models.TextField()

    def avaliarPassageiro(self):
        self.save()