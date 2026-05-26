from typing import Dict, List, Optional
from .database import Database

class UserModel:
    def __init__(self, db: Database):
        self.db = db
    
    def create_user(self, name: str, email: str, age: int) -> int:
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                (name, email, age)
            )
            return cursor.lastrowid
    
    def get_user(self, user_id: int) -> Optional[Dict]:
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            row = cursor.fetchone()
            return dict(row) if row else None
    
    def update_user(self, user_id: int, **kwargs) -> bool:
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            fields = [f"{k} = ?" for k in kwargs.keys()]
            values = list(kwargs.values()) + [user_id]
            cursor.execute(
                f"UPDATE users SET {', '.join(fields)} WHERE id = ?",
                values
            )
            return cursor.rowcount > 0

class OrderModel:
    def __init__(self, db: Database):
        self.db = db
    
    def create_order(self, user_id: int, product_name: str, 
                     quantity: int, total_price: float) -> int:
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO orders (user_id, product_name, quantity, total_price) 
                   VALUES (?, ?, ?, ?)""",
                (user_id, product_name, quantity, total_price)
            )
            return cursor.lastrowid
    
    def get_user_orders(self, user_id: int) -> List[Dict]:
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM orders WHERE user_id = ? ORDER BY id DESC",
                (user_id,)
            )
            return [dict(row) for row in cursor.fetchall()]
    
    def update_order_status(self, order_id: int, status: str) -> bool:
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE orders SET status = ? WHERE id = ?",
                (status, order_id)
            )
            return cursor.rowcount > 0