#coding:utf-8
from django.db import models

# Create your models here.
class Equipe(models.Model):
    """
    Representa uma equipe que participará de campeonatos
    """
    
    class Meta:
        verbose_name = "Equipe"
        verbose_name_plural = "Equipes"
    
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=3, unique=True)
    emblema = models.ImageField(upload_to="emblemas/")
    
    def __unicode__(self):
        
        return self.sigla
