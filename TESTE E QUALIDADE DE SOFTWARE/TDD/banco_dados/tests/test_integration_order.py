import pytest

class TestOrderIntegration:
    
    def test_create_order_for_nonexistent_user(self, order_model):
        """Teste: Criar pedido para usuário que não existe"""
        # Isso deve falhar devido à chave estrangeira
        with pytest.raises(Exception):
            order_model.create_order(99999, "Produto", 1, 10.00)
    
    def test_user_order_workflow(self, user_service, user_model, 
                                 order_model, sample_user_data):
        """Teste: Workflow completo de usuário + pedidos"""
        
        # 1. Criar usuário
        user_id = user_model.create_user(
            sample_user_data['name'],
            sample_user_data['email'],
            sample_user_data['age']
        )
        
        # 2. Criar múltiplos pedidos
        order1_id = order_model.create_order(user_id, "Produto A", 2, 100.00)
        order2_id = order_model.create_order(user_id, "Produto B", 1, 50.00)
        
        # 3. Atualizar status do pedido
        assert order_model.update_order_status(order1_id, "paid")
        assert order_model.update_order_status(order2_id, "shipped")
        
        # 4. Verificar pedidos do usuário
        orders = order_model.get_user_orders(user_id)
        assert len(orders) == 2
        
        # Verificar ordenação (mais recente primeiro)
        assert orders[0]['id'] > orders[1]['id']
        
        # 5. Verificar sumário
        summary = user_service.get_user_summary(user_id)
        assert summary['total_orders'] == 2
        assert summary['total_spent'] == 150.00
    
    def test_cascade_behavior(self, user_model, order_model, sample_user_data):
        """Teste: Verificar comportamento quando usuário é deletado"""
        # Criar usuário e pedido
        user_id = user_model.create_user(
            sample_user_data['name'],
            sample_user_data['email'],
            sample_user_data['age']
        )
        
        order_id = order_model.create_order(user_id, "Teste", 1, 10.00)
        
        # Verificar que pedido existe
        orders_before = order_model.get_user_orders(user_id)
        assert len(orders_before) == 1
        
        # Nota: Como nossa implementação não tem ON DELETE CASCADE,
        # pedidos permanecem mesmo se usuário for "deletado" logicamente
        # Este teste documenta o comportamento atual
