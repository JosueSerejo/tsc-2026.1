from typing import Dict, List, Optional
from .models import UserModel, OrderModel

class UserService:
    def __init__(self, user_model: UserModel, order_model: OrderModel):
        self.user_model = user_model
        self.order_model = order_model
    
    def register_user_with_orders(self, name: str, email: str, age: int,
                                  orders: List[Dict]) -> int:
        # Validação de negócio
        if age < 18:
            raise ValueError("User must be at least 18 years old")
        
        if not email or "@" not in email:
            raise ValueError("Invalid email format")
        
        # Criar usuário
        user_id = self.user_model.create_user(name, email, age)
        
        # Criar pedidos
        for order in orders:
            self.order_model.create_order(
                user_id,
                order['product_name'],
                order['quantity'],
                order['total_price']
            )
        
        return user_id
    
    def get_user_summary(self, user_id: int) -> Optional[Dict]:
        user = self.user_model.get_user(user_id)
        if not user:
            return None
        
        orders = self.order_model.get_user_orders(user_id)
        total_spent = sum(order['total_price'] for order in orders)
        
        return {
            'user': user,
            'total_orders': len(orders),
            'total_spent': total_spent,
            'last_order': orders[0] if orders else None
        }