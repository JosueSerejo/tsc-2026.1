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
        expect(conta.consultarSaldo()).toBe(1000);

    });

});


