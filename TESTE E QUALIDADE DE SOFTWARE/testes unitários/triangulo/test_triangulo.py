import pytest
import triangulo

def test_triangulo_equilatero():
    a = 5
    b = 5
    c = 5
    assert triangulo.triangulo_equilatero(a, b, c) == True

def test_triangulo_isoceles():
    a = 7
    b = 7
    c = 2
    assert triangulo.triangulo_isoceles(a, b, c) == True

def test_triangulo_escaleno():
    a = 1
    b = 2
    c = 3
    assert triangulo.triangulo_escaleno(a, b, c) == True

def test_triangulo_falso():
    a = 2
    b = 2
    c = 7
    assert triangulo.nao_e_triangulo(a, b, c) == True

def test_e_triangulo():
    a = 4
    b = 4
    c = 3
    assert triangulo.nao_e_triangulo(a, b, c) == False

def test_triangulo_com_zero_lados():
    a = 0
    b = 0
    c = 0
    assert triangulo.nao_e_triangulo(a, b, c) == True

def test_triangulo_com_dois_lados_zero():
    a = 0
    b = 0
    c = 5
    assert triangulo.nao_e_triangulo(a, b, c) == True

def test_triangulo_com_um_lado_zero():
    a = 0
    b = 5
    c = 5
    assert triangulo.nao_e_triangulo(a, b, c) == True

def test_triangulo_com_lados_negativos():
    a = -1
    b = 7
    c = 3
    assert triangulo.nao_e_triangulo(a, b, c) == True