from typing import Dict, List


class InsufficientStockException(Exception):
    """Exceção levantada quando a operação exige mais estoque do que o disponível."""


class ProductNotFoundException(Exception):
    """Exceção levantada quando um produto não é localizado no repositório."""


class Product:
    def __init__(self, product_id: str, name: str, price: float, quantity: int) -> None:
        if not product_id.strip():
            raise ValueError("O ID do produto não pode ser vazio.")
        if not name.strip():
            raise ValueError("O nome do produto não pode ser vazio.")
        if price <= 0:
            raise ValueError("O preço do produto não pode ser zero ou negativo.")
        if quantity < 0:
            raise ValueError("A quantidade de produtos não pode ser negativa.")

        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def decrease_stock(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError(
                "A quantidade para baixa de estoque deve ser maior que zero."
            )
        if self.quantity < amount:
            raise InsufficientStockException(
                f"Estoque insuficiente para o produto: {self.name}."
            )
        self.quantity -= amount

    def increase_stock(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError(
                "A quantidade para entrada de estoque deve ser maior que zero."
            )
        self.quantity += amount


class InventoryService:
    def __init__(self) -> None:
        self._products: Dict[str, Product] = {}

    def register_product(self, product: Product) -> None:
        if product.product_id in self._products:
            raise ValueError(
                f"O produto com ID {product.product_id} já está cadastrado."
            )
        self._products[product.product_id] = product

    def retrieve_product(self, product_id: str) -> Product:
        if product_id not in self._products:
            raise ProductNotFoundException(
                "Produto não localizado no sistema de inventário."
            )
        return self._products[product_id]

    def process_dispatch(self, product_id: str, amount: int) -> None:
        product = self.retrieve_product(product_id)
        product.decrease_stock(amount)

    def get_inventory_alerts(self, minimum_threshold: int = 10) -> List[Product]:
        return [
            product
            for product in self._products.values()
            if product.quantity < minimum_threshold
        ]