from unittest import TestCase
from operacoes import somar
from operacoes import subtrair
from operacoes import multiplicar
from operacoes import dividir

class TestOperacoes(TestCase):

    def test_somar_positivo(self):
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(1, 1), 2)

    def test_somar_negativo(self):
        self.assertEqual(somar(-2, -3), -5)
        self.assertEqual(somar(-1, -1), -2)

    def test_subtrair_positivo(self):
        self.assertEqual(subtrair(5, 2), 3)
        self.assertNotEqual(subtrair(10, 5), 9)

    def test_subtrair_negativos(self):
        