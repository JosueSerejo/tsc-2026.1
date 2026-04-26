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

});


