#coding:utf-8
from django.db import models
from campeonato.models import Jogo
from usuarios.models import Usuario
from datetime import datetime

class Palpite(models.Model):
    """
    Representa um palpite pra um jogo
    """
    
    jogo = models.ForeignKey(Jogo, related_name="palpites")
    usuario = models.ForeignKey(Usuario)
    golsMandante = models.IntegerField()
    golsVisitante = models.IntegerField()
    data = models.DateTimeField(editable = False, default = datetime.now())
    # Depois de realizado o jogo, os pontos serão armazenados aqui para não
    # precisarem ser calculados novamente
    pontos = models.IntegerField(editable = False)
    
    def __unicode__(self):
        return u"{0} {1} x {2} {3}".format(self.jogo.equipeMandante, self.golsMandante, self.golsVisitante, self.jogo.equipeVisitante)
    
    def acertouResultado(self):
        """
        Retorna True se o palpite acertou o resultado do jogo, mas não o placar
        """
        if self.jogo.realizado:
            acertouEmpate = self.golsMandante == self.golsVisitante and self.jogo.golsMandante == self.jogo.golsVisitante
            acertouVitoriaMandante = self.golsMandante > self.golsVisitante and self.jogo.golsMandante > self.jogo.golsVisitante
            acertouVitoriaVisitante = self.golsVisitante > self.golsMandante and self.jogo.golsVisitante > self.jogo.golsMandante
            
            return acertouEmpate or acertouVitoriaMandante or acertouVitoriaVisitante
        
        return None
    
    def acertouGolsMandante(self):
        """
        Retorna True se acertou os gols do mandante
        """
        if self.jogo.realizado:
            return self.golsMandante == self.jogo.golsMandante
        
        return None
    
    def acertouGolsVisitante(self):
        """
        Retorna True se acertou os gols do visitante
        """
        if self.jogo.realizado:
            return self.golsVisitante == self.jogo.golsVisitante
        
        return None
    
    def calcularPontos(self):
        """
        Calcula quantos pontos este palpite valeu
        """
        
        if self.jogo.realizado :
            
            pontosGanhos = 0;
        
            if self.acertouResultado():
                pontosGanhos += 5
            if self.acertouGolsMandante():
                pontosGanhos += 2
            if self.acertouGolsVisitante():
                pontosGanhos += 2
                
            # Se acertou tudo, ganha um ponto de bonus        
            if pontosGanhos == 9:
                pontosGanhos += 1
                
            return pontosGanhos
        
        return None
    
    def atualizarPontos(self):
        """
        Atualiza os pontos deste palpite
        """
        pontosGanhos = self.calcularPontos()
        if pontosGanhos is not None:
            self.pontos = pontosGanhos
            self.save()
                
    class Meta:
        verbose_name = "Palpite"
        verbose_name_plural = "Palpites"
        unique_together = (('jogo', 'usuario'),)
    