from avaliador import Avaliador
from lance import Lance
from leilao import Leilao
from usuario import Usuario

import unittest
from unittest import TestCase

class LeilaoTeste(TestCase):

    def test_deve_receber_um_lance(self):
        leilao = Leilao("Macbook Pro 15")
        self.assertEqual(0, len(leilao.get_lances()))
        leilao.propor(Lance(Usuario("Mari"), 2000.00))
        self.assertEqual(1, len(leilao.get_lances()))
        self.assertEqual(2000.00, leilao.get_lances()[0].valor)
    
    def test_deve_receber_varios_lances(self):
        leilao = Leilao("Macbook Pro 15")
        leilao.propor(Lance(Usuario("Mari"), 2000.00))
        leilao.propor(Lance(Usuario("jose"), 3000.00))
        self.assertEqual(2, len(leilao.get_lances()))
        self.assertEqual(2000.00, leilao.get_lances()[0].valor)
        self.assertEqual(3000.00, leilao.get_lances()[1].valor)
    
    def test_nao_pode_dois_lances_seguidos_de_usuario(self):
        leilao = Leilao("Macbook Pro 15")
        mari = Usuario("Mari")
        leilao.propor(Lance(mari, 2000.00))
        leilao.propor(Lance(mari, 3000.00))
        self.assertEqual(1, len(leilao.get_lances()))
        self.assertEqual(2000.00, leilao.get_lances()[0].valor)


if __name__ == "__main__":
    unittest.main()
