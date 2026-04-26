export class ContaBancaria {
  private saldo: number;

  constructor(
    public readonly numero: string,
    public readonly titular: string,
    saldoInicial: number = 0
  ) {
    if (saldoInicial < 0) {
      throw new Error('O saldo inicial não pode ser negativo.');
    }

    this.saldo = saldoInicial;
  }

  public consultarSaldo(): number {
    return this.saldo;
  }

  public depositar(valor: number): void {
    if (valor <= 0) {
      throw new Error('O valor do depósito deve ser maior que zero.');
    }

    this.saldo += valor;
  }

  public sacar(valor: number): void {
    if (valor <= 0) {
      throw new Error('O valor do saque deve ser maior que zero.');
    }

    if (valor > this.saldo) {
      throw new Error('Saldo insuficiente para saque.');
    }

    this.saldo -= valor;
  }

  public transferir(valor: number, contaDestino: ContaBancaria): void {
    if (contaDestino === this) {
      throw new Error('Não é possível transferir para a mesma conta.');
    }

    this.sacar(valor);
    contaDestino.depositar(valor);
  }
}