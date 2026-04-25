import pytest

from calculo import soma, subtracao, multiplicacao, divisao

def test_soma():
    assert soma(7,3) == 10

def test_subtracao():
    assert subtracao(5,4) == 1

def test_multiplicacao():
    assert multiplicacao(5,4) == 20

def test_divisao():
    assert divisao(10,2) == 5

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        divisao(10,0)