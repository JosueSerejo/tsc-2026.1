import pytest

from inventory import InsufficientStockException, Product, InventoryService, ProductNotFoundException

def test_initialization():
    product = Product("001", "vassoura", 5.0, 5)
    assert product.product_id == "001"
    assert product.name == "vassoura"
    assert product.price == 5.0
    assert product.quantity == 5

def test_without_id():
    with pytest.raises(ValueError):
            product = Product("","vassoura", 5.0, 5)

def test_without_name():
    with pytest.raises(ValueError):
            product = Product("001","", 5.0, 5)

def test_with_zero_price():
    with pytest.raises(ValueError):
            product = Product("001","vassoura", 0.0 , 5)

def test_with_negative_price():
    with pytest.raises(ValueError):
            product = Product("001","vassoura", -2.3 , 5)

def test_with_negative_quantitiy():
    with pytest.raises(ValueError):
            product = Product("001","vassoura", 2.3 , -3)

def test_register_product():
    invetory = InventoryService()
    product1 = Product("001", "vassoura", 5.0, 5)
    product2 = Product("002", "lapis", 3.0, 10)
    product3 = Product("003", "caneta", 2.50, 9)
    product4 = Product("004", "queijo", 9.0, 10)

    invetory.register_product(product1)
    invetory.register_product(product2)
    invetory.register_product(product3)
    invetory.register_product(product4)

def test_product_alredy_registered():
    invetory = InventoryService()
    product1 = Product("001", "vassoura", 5.0, 5)
    product2 = Product("002", "lapis", 3.0, 10)
    product3 = Product("003", "caneta", 2.50, 9)
    product4 = Product("004", "queijo", 9.0, 10)

    with pytest.raises(ValueError):
        invetory.register_product(product1)
        invetory.register_product(product2)
        invetory.register_product(product3) 
        invetory.register_product(product4)
        invetory.register_product(product2)

def test_increase_stock():
    inventory = InventoryService()
    product = Product("001", "vassoura", 5.0, 5)
    product.increase_stock(30)
    assert product.quantity == 35

def test_increase_stock_error():
    inventory = InventoryService()
    product = Product("001", "vassoura", 5.0, 5)
    with pytest.raises(ValueError):
        product.increase_stock(0)


def test_decrease_stock_with_insufficient_quantity():
    product = Product("001","vassoura",10.0,5)
    with pytest.raises(InsufficientStockException):
        product.decrease_stock(10)

def test_decrease_stock_with_zero_quantity():
    product = Product("001","vassoura",10.0,5)
    with pytest.raises(ValueError):
        product.decrease_stock(0)

def test_product_not_found():
    inventory = InventoryService()
    product1 = Product("001", "vassoura", 10.0, 5)
    product2 = Product("002", "lapis", 3.0, 10)
    
    inventory.register_product(product1)
    inventory.register_product(product2)

    with pytest.raises(ProductNotFoundException):
        inventory.retrieve_product("003")

def test_retrieve_product_success():
    inventory = InventoryService()
    product = Product("123", "Teclado Mechanical", 250.0, 50)
    inventory.register_product(product)

    retrieved = inventory.retrieve_product("123")

    assert retrieved.product_id == "123"
    assert retrieved.name == "Teclado Mechanical"
    assert retrieved.price == 250.0

def test_retrieve_product_not_found():
    inventory = InventoryService()

    with pytest.raises(ProductNotFoundException):
        inventory.retrieve_product("999")
