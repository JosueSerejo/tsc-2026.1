export interface Pedido {
  valorTotal: number;
  distanciaKm: number;
  cupom?: string;
}

export function processarPagamento(pedido: Pedido): number {
  // --- Validações (Exceções) ---
  
  if (pedido.valorTotal < 0) {
    throw new Error("O valor total do pedido não pode ser negativo.");
  }

  if (pedido.distanciaKm < 0) {
    throw new Error("A distância de entrega não pode ser negativa.");
  }

  if (pedido.cupom !== undefined && pedido.cupom !== 'QUERO50') {
    throw new Error("Cupom inválido: formato incorreto");
  }

  let valorFinal = pedido.valorTotal;

  // Regra 1: Desconto de 10% para compras acima de 500 reais
  if (pedido.valorTotal > 500) {
    valorFinal -= pedido.valorTotal * 0.1;
  }

  // Regra 2: Cupom fixo de 50 reais
  if (pedido.cupom === 'QUERO50') {
    if (valorFinal < 50) {
      throw new Error("O valor do pedido é insuficiente para aplicar este cupom.");
    }
    valorFinal -= 50;
  }

  // Regra 3: Taxa de entrega
  if (pedido.distanciaKm > 5) {
    valorFinal += pedido.distanciaKm * 2;
  }

  return valorFinal;
}