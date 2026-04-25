import {describe, it, expect} from 'vitest';
import { processarPagamento } from './ecommerce';

describe('processarPagamento', () => {


it('Deve aplicar 10% de desconto para pagamentos acima de 500', () => {
    const pedido = {valorTotal: 600, distanciaKm: 0};

    const valorFinal = processarPagamento(pedido);

    expect(valorFinal).toBe(540);

});

it('O valor da compra não apresenta desconto', () => {
    const pedido = {valorTotal: 400, distanciaKm: 0};

    const valorFinal = processarPagamento(pedido);

    expect(valorFinal).toBe(400);


})


});