import sqlite3
from config import DATABASE_PATH

class ProductManager:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.conn.cursor()
    
    def add_product(self, name, price, stock):
        self.cursor.execute('''
        INSERT INTO products (name, price, stock)
        VALUES (?, ?, ?)
        ''', (name, price, stock))
        self.conn.commit()
    
    def update_product(self, id, name, price, stock):
        self.cursor.execute('''
        UPDATE products
        SET name=?, price=?, stock=?
        WHERE id=?
        ''', (name, price, stock, id))
        self.conn.commit()
    
    def get_product(self, id):
        self.cursor.execute('SELECT * FROM products WHERE id=?', (id,))
        return self.cursor.fetchone()
    
    def get_all_products(self):
        self.cursor.execute('SELECT * FROM products')
        return self.cursor.fetchall()
    
    def update_stock(self, id, quantity):
        current_stock = self.get_product(id)[3]
        new_stock = current_stock - quantity
        self.cursor.execute('''
        UPDATE products
        SET stock=?
        WHERE id=?
        ''', (new_stock, id))
        self.conn.commit()