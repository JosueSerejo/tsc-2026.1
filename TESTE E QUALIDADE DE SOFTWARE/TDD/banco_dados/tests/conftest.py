import pytest
from src.database import Database
from src.models import UserModel, OrderModel
from src.services import UserService

@pytest.fixture
def db():
    """Cria banco de dados em memória para testes"""
    db = Database(":memory:")
    db.init_tables()
    return db

@pytest.fixture
def user_model(db):
    return UserModel(db)

@pytest.fixture
def order_model(db):
    return OrderModel(db)

@pytest.fixture
def user_service(user_model, order_model):
    return UserService(user_model, order_model)

@pytest.fixture
def sample_user_data():
    return {
        'name': 'João Silva',
        'email': 'joao@email.com',
        'age': 25
    }

@pytest.fixture
def sample_orders():
    return [
        {'product_name': 'Notebook', 'quantity': 1, 'total_price': 3500.00},
        {'product_name': 'Mouse', 'quantity': 2, 'total_price': 50.00},
        {'product_name': 'SSD', 'quantity': 1, 'total_price': 250.00}
    ]