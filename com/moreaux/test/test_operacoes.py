from unittest import TestCase
from com.moreaux.operacoes import Operacoes


class TestOperacoes(TestCase):
        
    def setUp(self):
        self.operacoes = Operacoes()

    def test_soma(self):
        self.assertEqual(self.operacoes.soma([1,5]), 5, "Should be 6")
