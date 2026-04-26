import { ContaBancaria } from "./contaBancaria";

export class BancoService {
  private contas: Map<string, ContaBancaria> = new Map();

  public criarConta(
    numero: string,
    titular: string,
    saldoInicial: number = 0
  ): ContaBancaria {
    if (this.contas.has(numero)) {
      throw new Error('Já existe uma conta com este número.');
    }

    const conta = new ContaBancaria(numero, titular, saldoInicial);
    this.contas.set(numero, conta);

    return conta;
  }

  public buscarConta(numero: string): ContaBancaria {
    const conta = this.contas.get(numero);

    if (!conta) {
      throw new Error('Conta não encontrada.');
    }

    return conta;
  }

  public listarContas(): ContaBancaria[] {
    return Array.from(this.contas.values());
  }

  public transferir(
    numeroOrigem: string,
    numeroDestino: string,
    valor: number
  ): void {
    const origem = this.buscarConta(numeroOrigem);
    const destino = this.buscarConta(numeroDestino);

    origem.transferir(valor, destino);
  }
}