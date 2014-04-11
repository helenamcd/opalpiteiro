#coding:utf-8
from django.db import models

class Campeonato(models.Model):
    """
    Representa um campeonato que poderá ser realizado um bolão
    """
    class Meta:
        verbose_name = "Campeonato"
        verbose_name_plural = "Campeonatos"

    nome = models.CharField(max_length=100)
    ativo = models.BooleanField("Ativo")
    dataInicio = models.DateField("Início")
    dataTermino = models.DateField("Término")
    
    def __unicode__(self):
        return self.nome
    
