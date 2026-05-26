import pytest
from src.services import UserService

class TestUserIntegration:
    
    def test_create_user_success(self, user_service, sample_user_data):
        """Teste: Criar usuário com dados válidos"""
        user_id = user_service.user_model.create_user(
            sample_user_data['name'],
            sample_user_data['email'],
            sample_user_data['age']
        )
        
        # Verificar se usuário foi criado
        user = user_service.user_model.get_user(user_id)
        assert user is not None
        assert user['name'] == sample_user_data['name']
        assert user['email'] == sample_user_data['email']
        assert user['age'] == sample_user_data['age']
    
    def test_create_duplicate_email(self, user_service, sample_user_data):
        """Teste: Tentar criar dois usuários com mesmo email"""
        # Primeiro usuário
        user_service.user_model.create_user(
            sample_user_data['name'],
            sample_user_data['email'],
            sample_user_data['age']
        )
        
        # Segundo usuário com mesmo email
        with pytest.raises(Exception):  # SQLite unique constraint violation
            user_service.user_model.create_user(
                "Outro Nome",
                sample_user_data['email'],  # Mesmo email
                30
            )
    
    def test_register_user_with_orders_integration(self, user_service, 
                                                     sample_user_data, 
                                                     sample_orders):
        """Teste: Registro completo de usuário com pedidos"""
        user_id = user_service.register_user_with_orders(
            sample_user_data['name'],
            sample_user_data['email'],
            sample_user_data['age'],
            sample_orders
        )
        
        # Verificar sumário do usuário
        summary = user_service.get_user_summary(user_id)
        
        assert summary is not None
        assert summary['total_orders'] == 3
        assert summary['total_spent'] == 3800.00
        assert summary['user']['email'] == sample_user_data['email']
    
    def test_register_underage_user(self, user_service, sample_orders):
        """Teste: Tentar registrar usuário menor de idade"""
        with pytest.raises(ValueError, match="must be at least 18"):
            user_service.register_user_with_orders(
                "João Jr.",
                "joaojr@email.com",
                16,  # Menor de idade
                sample_orders
            )
    
    def test_invalid_email(self, user_service, sample_orders):
        """Teste: Tentar registrar com email inválido"""
        with pytest.raises(ValueError, match="Invalid email"):
            user_service.register_user_with_orders(
                "Maria",
                "email-invalido",  # Email sem @
                25,
                sample_orders
            )
    
    def test_update_user_and_verify_orders(self, user_service, 
                                           sample_user_data,
                                           order_model):
        """Teste: Atualizar usuário e verificar que pedidos permanecem"""
        # Criar usuário
        user_id = user_service.user_model.create_user(
            sample_user_data['name'],
            sample_user_data['email'],
            sample_user_data['age']
        )
        
        # Criar pedido
        order_id = order_model.create_order(user_id, "Produto Teste", 2, 50.00)
        
        # Atualizar usuário
        user_service.user_model.update_user(user_id, name="Nome Atualizado")
        
        # Verificar que pedido ainda existe e está associado
        orders = order_model.get_user_orders(user_id)
        assert len(orders) == 1
        assert orders[0]['id'] == order_id
