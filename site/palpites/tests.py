from django.test import TestCase

from campeonato.models import Jogo
from palpites.models import Palpite


class PalpiteTestCase(TestCase):
    """
    TestCase para os palpites
    """

    fixtures = ['equipes', 'campeonato']
    
    # ACERTOU RESULTADO
        
    def testAcertouResultadoPalpite3x0Jogo3x0(self):
    
        jogo = Jogo(golsMandante = 3, golsVisitante = 0, realizado = True)    
        palpite = Palpite(jogo = jogo, golsMandante = 3, golsVisitante = 0)
        
        self.assertTrue(palpite.acertouResultado())
        
    def testAcertouResultadoPalpite2x1Jogo3x0(self):

        jogo = Jogo(golsMandante = 3, golsVisitante = 0, realizado = True)        
        palpite = Palpite(jogo = jogo, golsMandante = 2, golsVisitante = 1)
        
        self.assertTrue(palpite.acertouResultado())
        
    def testAcertouResultadoPalpite1x1Jogo3x0(self):
        
        jogo = Jogo(golsMandante = 3, golsVisitante = 0, realizado = True)
        palpite = Palpite(jogo = jogo, golsMandante = 1, golsVisitante = 1)
        
        self.assertFalse(palpite.acertouResultado())
        
    def testAcertouResultadoPalpite1x2Jogo3x0(self):
        
        jogo = Jogo(golsMandante = 3, golsVisitante = 0, realizado = True)
        palpite = Palpite(jogo = jogo, golsMandante = 1, golsVisitante = 2)
        
        self.assertFalse(palpite.acertouResultado())
        
    def testAcertouResultadoPalpite2x2Jogo1x1(self):
        
        jogo = Jogo(golsMandante = 1, golsVisitante = 1, realizado = True)
        palpite = Palpite(jogo = jogo, golsMandante = 2, golsVisitante = 2)
        
        self.assertTrue(palpite.acertouResultado())
        
    def testAcertouResultadoPalpite0x2Jogo1x3(self):
        
        jogo = Jogo(golsMandante = 1, golsVisitante = 3, realizado = True)
        palpite = Palpite(jogo = jogo, golsMandante = 0, golsVisitante = 2)
        
        self.assertTrue(palpite.acertouResultado())
        
    def testAcertouResultadoJogoNaoRealizado(self):
        
        jogo = Jogo(golsMandante = 1, golsVisitante = 3)
        palpite = Palpite(jogo = jogo, golsMandante = 0, golsVisitante = 2)
        
        self.assertIsNone(palpite.acertouResultado())
        
    # ACERTOU GOLS MANDANTE
    def testAcertouGolsMandantePalpite3x0Jogo3x2(self):
        
        jogo = Jogo(golsMandante = 3, golsVisitante = 2, realizado = True)
        palpite = Palpite(jogo = jogo, golsMandante = 3, golsVisitante = 0)
                
        self.assertTrue(palpite.acertouGolsMandante())
        
    def testAcertouGolsMandantePalpite3x0Jogo3x3(self):
        
        jogo = Jogo(golsMandante = 3, golsVisitante = 3, realizado = True)
        palpite = Palpite(jogo = jogo, golsMandante = 3, golsVisitante = 0)
        
        self.assertTrue(palpite.acertouGolsMandante())
    
    def testAcertouGolsMandantePalpite3x0Jogo2x3(self):
        
        jogo = Jogo(golsMandante = 2, golsVisitante = 3, realizado = True)
        palpite = Palpite(jogo = jogo, golsMandante = 3, golsVisitante = 0)
        
        self.assertFalse(palpite.acertouGolsMandante())
        
    def testAcertouGolsMandanteJogoNaoRealizado(self):
        
        jogo = Jogo(golsMandante = 2, golsVisitante = 3)
        palpite = Palpite(jogo = jogo, golsMandante = 2, golsVisitante = 0)
        
        self.assertIsNone(palpite.acertouGolsMandante())
        
    # ACERTOU GOLS VISITANTE
    def testAcertouGolsVisitantePalpite2x2Jogo3x2(self):
        
        jogo = Jogo(golsMandante = 3, golsVisitante = 2, realizado = True)
        palpite = Palpite(jogo = jogo, golsMandante = 2, golsVisitante = 2)
        
        self.assertTrue(palpite.acertouGolsVisitante())
        
    def testAcertouGolsVisitantePalpite3x0Jogo0x0(self):
        
        jogo = Jogo(golsMandante = 0, golsVisitante = 0, realizado = True)
        palpite = Palpite(jogo = jogo, golsMandante = 3, golsVisitante = 0)
        
        self.assertTrue(palpite.acertouGolsVisitante())
    
    def testAcertouGolsVisitantePalpite2x0Jogo2x3(self):
        
        jogo = Jogo(golsMandante = 2, golsVisitante = 3, realizado = True)
        palpite = Palpite(jogo = jogo, golsMandante = 2, golsVisitante = 0)
        
        self.assertFalse(palpite.acertouGolsVisitante())
        
    def testAcertouGolsVisitanteJogoNaoRealizado(self):
        
        jogo = Jogo(golsMandante = 2, golsVisitante = 3)
        palpite = Palpite(jogo = jogo, golsMandante = 2, golsVisitante = 0)
        
        self.assertIsNone(palpite.acertouGolsVisitante())
        
    # CALCULAR PONTOS
    
    def testCalcularPontosPalpite3x0Jogo3x0(self):
        
        jogo = Jogo(golsMandante = 3, golsVisitante = 0, realizado = True)
        palpite = Palpite(jogo = jogo, golsMandante = 3, golsVisitante = 0)
        
        self.assertEquals(10, palpite.calcularPontos())
    
    def testCalcularPontosPalpite3x0Jogo2x1(self):
        
        jogo = Jogo(golsMandante = 2, golsVisitante = 1, realizado = True)
        palpite = Palpite(jogo = jogo, golsMandante = 3, golsVisitante = 0)
        
        self.assertEquals(5, palpite.calcularPontos())
        
    def testCalcularPontosPalpite3x0Jogo2x0(self):
        
        jogo = Jogo(golsMandante = 2, golsVisitante = 0, realizado = True)
        palpite = Palpite(jogo = jogo, golsMandante = 3, golsVisitante = 0)
        
        self.assertEquals(7, palpite.calcularPontos())
        
    def testCalcularPontosPalpite3x1Jogo3x0(self):
        
        jogo = Jogo(golsMandante = 3, golsVisitante = 0, realizado = True)
        palpite = Palpite(jogo = jogo, golsMandante = 3, golsVisitante = 1)
        
        self.assertEquals(7, palpite.calcularPontos())
        
    def testCalcularPontosPalpite3x1Jogo3x3(self):
        
        jogo = Jogo(golsMandante = 3, golsVisitante = 3, realizado = True)
        palpite = Palpite(jogo = jogo, golsMandante = 3, golsVisitante = 1)
        
        self.assertEquals(2, palpite.calcularPontos())
        
    def testCalcularPontosPalpite1x1Jogo2x2(self):
        
        jogo = Jogo(golsMandante = 2, golsVisitante = 2, realizado = True)
        palpite = Palpite(jogo = jogo, golsMandante = 1, golsVisitante = 1)
        
        self.assertEquals(5, palpite.calcularPontos())
        
    def testCalcularPontosPalpite2x2Jogo2x2(self):
        
        jogo = Jogo(golsMandante = 2, golsVisitante = 2, realizado = True)
        palpite = Palpite(jogo = jogo, golsMandante = 2, golsVisitante = 2)
        
        self.assertEquals(10, palpite.calcularPontos())
        
    def testCalcularPontosPalpite1x2Jogo2x2(self):
        
        jogo = Jogo(golsMandante = 2, golsVisitante = 2, realizado = True)
        palpite = Palpite(jogo = jogo, golsMandante = 1, golsVisitante = 2)
        
        self.assertEquals(2, palpite.calcularPontos())
        
        
    def testCalcularPontosPalpite1x2Jogo2x3(self):
        
        jogo = Jogo(golsMandante = 2, golsVisitante = 3, realizado = True)
        palpite = Palpite(jogo = jogo, golsMandante = 1, golsVisitante = 2)
        
        self.assertEquals(5, palpite.calcularPontos())
        
    def testCalcularPontosJogoNaoRealizado(self):
        
        jogo = Jogo(golsMandante = 2, golsVisitante = 3)
        palpite = Palpite(jogo = jogo, golsMandante = 1, golsVisitante = 2)
        
        self.assertIsNone(palpite.calcularPontos())