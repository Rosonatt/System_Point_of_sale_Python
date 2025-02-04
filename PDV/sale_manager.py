import sqlite3
from datetime import datetime
from config import DATABASE_PATH

class SaleManager:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.conn.cursor()
    
    def create_sale(self, items):
       
        total_amount = 0
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
    
        self.cursor.execute('''
        INSERT INTO sales (date, total_amount)
        VALUES (?, ?)
        ''', (date, total_amount))
        sale_id = self.cursor.lastrowid
        
        
        for product_id, quantity in items:
            
            self.cursor.execute('SELECT price FROM products WHERE id=?', (product_id,))
            price = self.cursor.fetchone()[0]
            
  
            self.cursor.execute('''
            INSERT INTO sale_items (sale_id, product_id, quantity, price)
            VALUES (?, ?, ?, ?)
            ''', (sale_id, product_id, quantity, price))
            
            total_amount += price * quantity
        
        
        self.cursor.execute('''
        UPDATE sales
        SET total_amount=?
        WHERE id=?
        ''', (total_amount, sale_id))
        
        self.conn.commit()
        return sale_id
    
    def get_sale(self, id):
        self.cursor.execute('SELECT * FROM sales WHERE id=?', (id,))
        return self.cursor.fetchone()