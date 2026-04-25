import pytest

from banco import ContaBancaria

def test_depositar():
    conta = ContaBancaria()
    conta.depositar(100)
    assert conta.saldo == 100

def test_deposito_invalido():
    conta = ContaBancaria()
    with pytest.raises(ValueError):
        conta.depositar(-50)


def test_sacar():
    conta = ContaBancaria(200)
    conta.sacar(50)
    assert conta.saldo == 150


def test_sacar_saldo_insuficiente():
    conta = ContaBancaria(800)
    with pytest.raises(ValueError):
        conta.sacar(900)


def test_sacar_valor_invalido():
    conta = ContaBancaria(800)
    with pytest.raises(ValueError):
        conta.sacar(0)


def test_saque_invalido():
    conta = ContaBancaria(100)
    with pytest.raises(ValueError):
        conta.sacar(200)

def test_transferencia():
    conta1 = ContaBancaria()
    conta2 = ContaBancaria()

    conta1.depositar(300)
    conta1.transferir(conta2, 100)

    assert conta2.saldo == 100

def test_transferir_duas_contas():
    conta1 = ContaBancaria()
    conta2 = ContaBancaria()
    conta3 = ContaBancaria()

    conta1.depositar(800)
    conta1.transferir(conta2, 400)
    conta1.transferir(conta3, 200)

    assert conta1.saldo == 200
    assert conta2.saldo == 400
    assert conta3.saldo == 200

def test_saldo_invalido():
    conta1 = ContaBancaria()
    conta2 = ContaBancaria()

    conta1.depositar(500)
    with pytest.raises(ValueError):
        conta1.transferir(conta2,600)

def test_valor_inválido():
    conta1 = ContaBancaria()
    conta2 = ContaBancaria()

    conta1.depositar(700)
    with pytest.raises(ValueError):
        conta1.transferir(conta2, 0)
        
def test_tansferir_de_duas_contas():
    conta1 = ContaBancaria()
    conta2 = ContaBancaria()
    conta3 = ContaBancaria()

    conta2.depositar(600)
    conta3.depositar(900)
    
    conta2.transferir(conta1,300)
    conta3.transferir(conta1,700)

    conta1.saldo == 1000
