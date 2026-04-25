import pytest

from usuario import Usuario

def test_maior_de_idade():
    usuario = Usuario("Maria", 20)
    assert usuario.eh_maior_de_idade() == True

def test_menor_de_idade():
    usuario = Usuario("Gabriel", 17)
    assert usuario.eh_maior_de_idade() == False

def teste_atualizar_idade():
    usuario = Usuario("João", 17)
    usuario.atualizar_idade(18)
    assert usuario.eh_maior_de_idade() == True

def test_idade_invalida():
    usuario = Usuario("Jonas", 20)
    with pytest.raises(ValueError):
        usuario.atualizar_idade(-5)

def test_aniversario_errado():
    usuario = Usuario("Leandra", 44)
    with pytest.raises(ValueError):
        usuario.atualizar_idade(46)