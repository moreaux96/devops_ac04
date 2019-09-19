from unittest import TestCase
from com.moreaux.operacoes import Operacoes


class TestOperacoes(TestCase):
        
    def setUp(self):
        self.operacoes = Operacoes()

    def test_velocidade(self):
        self.assertEqual(self.operacoes.velocidade([100,20]),"Should be velocidade: 5 m/s")
