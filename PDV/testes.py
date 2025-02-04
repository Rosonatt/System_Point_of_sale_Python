# tests.py
import unittest
from product_manager import ProductManager
from sale_manager import SaleManager
import os
from config import DATABASE_PATH

class TestPDVSystem(unittest.TestCase):
    def setUp(self):
        # Criar banco de dados de teste
        if os.path.exists(DATABASE_PATH):
            os.remove(DATABASE_PATH)
        from config import create_database
        create_database()
        
        self.product_manager = ProductManager()
        self.sale_manager = SaleManager()
    
    def test_add_product(self):
        self.product_manager.add_product("Teste", 10.0, 100)
        product = self.product_manager.get_product(1)
        self.assertEqual(product[1], "Teste")
        self.assertEqual(product[2], 10.0)
        self.assertEqual(product[3], 100)
    
    def test_create_sale(self):
        # Adicionar produto
        self.product_manager.add_product("Teste", 10.0, 100)
        
        # Criar venda
        items = [(1, 2)]  # 2 unidades do produto 1
        sale_id = self.sale_manager.create_sale(items)
        
        # Verificar venda
        sale = self.sale_manager.get_sale(sale_id)
        self.assertEqual(sale[2], 20.0)  # total amount
    
    def tearDown(self):
        if os.path.exists(DATABASE_PATH):
            os.remove(DATABASE_PATH)

if __name__ == '__main__':
    unittest.main()