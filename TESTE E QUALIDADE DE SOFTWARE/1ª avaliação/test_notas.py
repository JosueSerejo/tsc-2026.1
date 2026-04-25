import pytest
from notas import analisar_notas

def test_media_e_mediana():
    """Calcula a média e a mediana de notas da turma"""
    notas = [7.5, 8.0, 6.0, 9.0, 5.5]
    resultado = analisar_notas(notas)
    assert resultado['media'] == 7.2
    assert resultado['mediana'] == 7.5

def test_maior_e_menor_nota():
    """Indica qual a maior e a menor nota da turma"""
    notas = [8.9, 9.0, 4.2, 6.5,7.8]
    resultado = analisar_notas(notas)
    assert resultado['maior'] == 9.0
    assert resultado['menor'] == 4.2

def test_aprovados_e_reprovados():
    """Retorna quantos alunos foram aprovados e reprovados"""
    notas = [8.9, 9.0, 4.2, 5.5,7.2]
    resultado = analisar_notas(notas)
    assert resultado['aprovados'] == 3
    assert resultado['reprovados'] == 2

def test_classificacao_das_turmas():
    """Retorna os níveis de classificação da turma de acordo com a sua média"""
    assert analisar_notas([8.0, 9.3, 7.8])['situacao_turma'] == 'A'
    assert analisar_notas([5.5, 4.7, 8.2])['situacao_turma'] == 'B'
    assert analisar_notas([3.5, 4.7, 2.3])['situacao_turma'] == 'C'

def test_elemento_nao_numerico():
    """Retorna um erro de elemento não numérico"""
    with pytest.raises(TypeError):
        analisar_notas([7.5, '8.0', 6.0])

def test_lista_vazia():
    """Retorna um erro de lista vazia"""
    with pytest.raises(ValueError):
        analisar_notas([])

def test_nota_negativa():
    """Retorna um erro de valor fora do intervalo (Valor negativo)"""
    with pytest.raises(ValueError):
        analisar_notas([5.2, -7.3, 9.0])

def test_nota_maior_que_dez():
    """Retorna um erro de valor fora do intervalo (valor acima de 10)"""
    with pytest.raises(ValueError):
        analisar_notas([7.5, 10.6, 6.0])