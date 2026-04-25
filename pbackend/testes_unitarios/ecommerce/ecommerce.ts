interface Pedido {
  valorTotal: number;
  distanciaKm: number;
  cupom?: string;
}

export function processarPagamento(pedido: Pedido): number {
  let valorFinal = pedido.valorTotal;

  // Regra 1: Desconto de 10% para compras acima de 500 reais
  if (pedido.valorTotal > 500) {
    valorFinal -= pedido.valorTotal * 0.1;
  }

  // Regra 2: Cupom fixo de 50 reais
  if (pedido.cupom === 'QUERO50') {
    valorFinal -= 50;
  }

  // Regra 3: Taxa de entrega (Grátis se for menos de 5km, senão 2 reais por km)
  if (pedido.distanciaKm > 5) {
    valorFinal += pedido.distanciaKm * 2;
  }

  return valorFinal;
}