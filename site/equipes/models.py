#coding:utf-8
from django.db import models

# Create your models here.
class Equipe(models.Model):
    """
    Representa uma equipe que participará de campeonatos
    """
    nome = models.CharField(max_length=100)
    
    def __unicode__(self):
        
        return self.nome
