import {describe, it, expect} from 'vitest';
import { processarPagamento } from './ecommerce';

describe('processarPagamento', () => {


it('Deve aplicar 10% de desconto para pagamentos acima de 500', () => {
    const pedido = {valorTotal: 600, distanciaKm: 0};

    const valorFinal = processarPagamento(pedido);

    expect(valorFinal).toBe(540);

});

it('Não deve apresenta desconto na compra', () => {
    const pedido = {valorTotal: 400, distanciaKm: 0};

    const valorFinal = processarPagamento(pedido);

    expect(valorFinal).toBe(400);


})

it('Deve ser aplicado o cupom de -50 reais', () => {
    const pedido = {valorTotal: 300, distanciaKm: 0, cupom:'QUERO50'};

    const valorFinal = processarPagamento(pedido);

    expect(valorFinal).toBe(250)
});

it('Não deve ser aplicado cupom caso seja inválido', () => {
    const pedido =  {valorTotal: 200, distanciaKm: 0, cupom:'QUERO5'};

    const valorFinal = processarPagamento(pedido);

    expect(valorFinal).toBe(200);
}); 

it('Deve aplicar a taxa de entrega', () => {
    const pedido = {valorTotal: 500, distanciaKm: 10};

    const valorFinal = processarPagamento(pedido);

    expect(valorFinal).toBe(520);

});

it('Deve aplicar taxa de entrega e cupons aplicados', () => {
    const pedido = {valorTotal: 1000, distanciaKm: 10, cupom: 'QUERO50'};

    const valorFinal = processarPagamento(pedido);

    expect(valorFinal).toBe(870)



});

});