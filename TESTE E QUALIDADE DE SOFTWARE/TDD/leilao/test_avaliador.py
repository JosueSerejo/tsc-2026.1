from avaliador import Avaliador
from usuario import Usuario
from leilao import Leilao
from lance import Lance

import pytest

def test_avaliador_crescente():
    joao = Usuario("João")
    rita = Usuario("Rita")
    jose = Usuario("Jose")
    mari = Usuario("Mari")
    leilao = Leilao("Smart Phone Samsung 32")
    leilao.propor(Lance(mari, 150.00))
    leilao.propor(Lance(joao, 300.00))
    leilao.propor(Lance(jose, 400.00))
    leilao.propor(Lance(rita, 450.00))
    leiloeiro = Avaliador()
    leiloeiro.avaliar(leilao)
    assert leiloeiro.get_maior_lance() == 450

def test_avaliador_decrescente():
    joao = Usuario("João")
    rita = Usuario("Rita")
    jose = Usuario("Jose")
    mari = Usuario("Mari")
    leilao = Leilao("Smart Phone Samsung 32")
    leilao.propor(Lance(rita, 450.00))
    leilao.propor(Lance(jose, 400.00))
    leilao.propor(Lance(joao, 300.00))
    leilao.propor(Lance(mari, 150.00))
    leiloeiro = Avaliador()
    leiloeiro.avaliar(leilao)
    assert leiloeiro.get_maior_lance() == 450

def test_avaliador_iguais():
    joao = Usuario("João")
    rita = Usuario("Rita")
    jose = Usuario("Jose")
    mari = Usuario("Mari")
    leilao = Leilao("Smart Phone Samsung 32")
    leilao.propor(Lance(rita, 100.00))
    leilao.propor(Lance(jose, 100.00))
    leilao.propor(Lance(joao, 100.00))
    leilao.propor(Lance(mari, 100.00))
    leiloeiro = Avaliador()
    leiloeiro.avaliar(leilao)
    assert leiloeiro.get_maior_lance() == 100

def test_avaliador_vazia():
    leilao = Leilao("Smart Phone Samsung 32")
    leiloeiro = Avaliador()
    leiloeiro.avaliar(leilao)
    assert leiloeiro.get_maior_lance() == -10 ** 101

def test_avaliador_negativo():
    joao = Usuario("João")
    rita = Usuario("Rita")
    jose = Usuario("Jose")
    mari = Usuario("Mari")
    leilao = Leilao("Smart Phone Samsung 32")
    leilao.propor(Lance(rita, 450.00))
    leilao.propor(Lance(jose, 400.00))
    leilao.propor(Lance(joao, -300.00))
    leilao.propor(Lance(mari, 150.00))
    leiloeiro = Avaliador()
    leiloeiro.avaliar(leilao)
    assert leiloeiro.get_menor_lance() == -300
    # Algo deu errado aqui!!