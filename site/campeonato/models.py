#coding:utf-8
from django.db import models

from equipes.models import Equipe
from django.db.models.signals import post_save


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
    
class Fase(models.Model):
    """
    Representa a fase de um campeonato
    """
    
    class Meta:
        verbose_name = "Fase"
        verbose_name_plural = "Fases"
    
    nome = models.CharField(max_length=100)
    campeonato = models.ForeignKey(Campeonato)
    
    def __unicode__(self):
        
        return self.nome
    
class Grupo(models.Model):
    """
    Representa o(s) grupo(s) formados para uma fase do campeonato
    """
    
    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"
    
    nome = models.CharField(max_length=100)
    fase = models.ForeignKey(Fase)
    equipes = models.ManyToManyField(Equipe, through="TabelaGrupo")
    
    def __unicode__(self):
        return self.nome
        
class Rodada(models.Model):
    """
    Representa uma rodada que ocorre em um grupo
    """
    
    class Meta:
        verbose_name = "Rodada"
        verbose_name_plural = "Rodadas"
    
    nome = models.CharField(max_length = 50)
    grupo = models.ForeignKey(Grupo)
    
    def __unicode__(self):
        return self.nome
        
class Jogo(models.Model):
    """ 
    Classe que representa uma partida entre duas equipes. Esta partida deve ocorrer em uma rodada
    """
    
    class Meta:
        verbose_name = "Jogo"
        verbose_name_plural = "Jogos"
    
    identificacao = models.CharField(max_length=30)
    rodada = models.ForeignKey(Rodada, related_name='jogos')
    equipeMandante = models.ForeignKey(Equipe, related_name="mandantes")
    equipeVisitante = models.ForeignKey(Equipe, related_name="visitantes")
    golsMandante = models.IntegerField(default = 0)
    golsVisitante = models.IntegerField(default = 0)
    amarelosMandante = models.IntegerField(default = 0)
    amarelosVisitante = models.IntegerField(default = 0)
    vermelhosMandante = models.IntegerField(default = 0)
    vermelhosVisitante = models.IntegerField(default = 0)
    data = models.DateTimeField("Data e Hora")
    local = models.CharField(max_length=100, blank = True, null = True)
    realizado = models.BooleanField("Jogo realizado", default = False)
    
    def __unicode__(self):
        return u"{0} - {1} {2} x {3} {4}".format(self.identificacao, self.equipeMandante, self.golsMandante, self.golsVisitante, self.equipeVisitante)
    
    
def atualizarPalpites(sender, **kwargs):
    """
    Sinal 'post_save' para atualizar os pontos de cada palpite
    """
    jogo = kwargs.get('instance')
    if jogo.realizado :
        for palpite in jogo.palpites.all():
            palpite.atualizarPontos()

post_save.connect(atualizarPalpites, Jogo)

#--------------------------------------------------------------

class TabelaGrupo(models.Model):
    """
    Representa a tabela de classificação de um grupo. Apesar de alguns campos aqui serem resultados de cálculos,
    irá tornar o banco mais ágil 
    """
    
    class Meta:
        verbose_name = "Tabela"
        verbose_name_plural = "Tabelas"
        unique_together = (('grupo', 'equipe'),)
        
    grupo = models.ForeignKey(Grupo)
    equipe = models.ForeignKey(Equipe)
    pontos = models.IntegerField(default = 0)
    golsPro = models.IntegerField(default = 0)
    golsContra = models.IntegerField(default = 0)
    saldoGols = models.IntegerField(default = 0)
    vitorias = models.IntegerField(default = 0)
    derrotas = models.IntegerField(default = 0)
    empates = models.IntegerField(default = 0)
    totalAmarelos = models.IntegerField(default = 0)
    totalVermelhos = models.IntegerField(default = 0)    
            
    def __unicode__(self):
        return self.equipe