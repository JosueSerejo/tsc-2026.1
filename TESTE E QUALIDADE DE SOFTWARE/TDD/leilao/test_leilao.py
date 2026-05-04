from avaliador import Avaliador
from lance import Lance
from leilao import Leilao
from usuario import Usuario

import unittest

class TestLeilao(unittest.TestCase):

    def setUp(self):
        self.avaliador = Avaliador()
        self.usuario1 = Usuario('João')
        self.usuario2 = Usuario('Maria')
        self.usuario3 = Usuario('Pedro')

    def test_avaliar_leilao(self):
        leilao = Leilao('PlayStation 5')
        leilao.propor(Lance(self.usuario1, 2000))
        leilao.propor(Lance(self.usuario2, 2500))
        leilao.propor(Lance(self.usuario3, 3000))

        self.avaliador.avalia(leilao)

        self.assertEqual(2000, self.avaliador.menor_lance)
        self.assertEqual(3000, self.avaliador.maior_lance)