#coding:utf-8
from django.db import models
from campeonato.models import Jogo
from usuarios.models import Usuario

class Palpite(models.Model):
    """
    Representa um palpite pra um jogo
    """
    
    jogo = models.ForeignKey(Jogo)
    usuario = models.ForeignKey(Usuario)
    golsMandante = models.IntegerField()
    golsVisitante = models.IntegerField()
    data = models.DateTimeField()
    
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
            
            total_pontos = 0;
        
            if self.acertouResultado():
                total_pontos += 5
            if self.acertouGolsMandante():
                total_pontos += 2
            if self.acertouGolsVisitante():
                total_pontos += 2
                
            # Se acertou tudo, ganha um ponto de bonus        
            if total_pontos == 9:
                total_pontos += 1
                
            return total_pontos
        
        return None
                
    class Meta:
        verbose_name = "Palpite"
        verbose_name_plural = "Palpites"
        unique_together = (('jogo', 'usuario'),)
    