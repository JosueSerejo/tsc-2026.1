import {describe, it, expect, beforeEach} from 'vitest';
import { ContaBancaria } from '../src/contaBancaria';

describe('ContaBancaria', () => {
    let conta: ContaBancaria;

    beforeEach(() => {
        conta = new ContaBancaria('12345', 'João Silva', 1000);
    });

    it('Deve criar a conta com os dados corretos', () => { 
        expect(conta.numero).toBe('12345');
        expect(conta.titular).toBe('João Silva');
    });

    it('Deve retornar o saldo correto', () => { 
        expect(conta.consultarSaldo()).toBe(1000);
    });


    it('Deve retornar o valor final com o deposito', () => {
        conta.depositar(300);
        expect(conta.consultarSaldo()).toBe(1300);

    });

    it('Deve retornar o valor correto após o saque', () => { 
        conta.sacar(500)
        expect(conta.consultarSaldo()).toBe(500)

    });

    it('Deve transferir valor entre duas contas', () => { 
        const conta2 = new ContaBancaria('12365', 'Maria Silva', 1000);
        conta.transferir(200, conta2);
        expect(conta.consultarSaldo()).toBe(800);
        expect(conta2.consultarSaldo()).toBe(1200);
    });


    it('Deve transferir valor entre três contas', () => { 
        const conta2 = new ContaBancaria('12365', 'Maria Silva', 1000);
        const conta3 = new ContaBancaria('18365', 'Gael Silva', 6000);
        conta.transferir(200, conta2);
        conta.transferir(200, conta3);
        conta3.transferir(500, conta2);
        expect(conta.consultarSaldo()).toBe(600);
        expect(conta2.consultarSaldo()).toBe(1700);
        expect(conta3.consultarSaldo()).toBe(5700);
    });

});


