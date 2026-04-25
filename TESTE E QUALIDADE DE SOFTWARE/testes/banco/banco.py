class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor inválido")
        self.saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor inválido")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= valor

    def transferir(self, outra_conta, valor):
        if valor <= 0:
            raise ValueError("Valor inválido")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")

        self.saldo -= valor
        outra_conta.saldo += valor