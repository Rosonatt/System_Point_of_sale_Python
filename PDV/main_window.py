# main_window.py
import tkinter as tk
from tkinter import ttk, messagebox
from product_manager import ProductManager
from sale_manager import SaleManager

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema PDV")
        self.root.geometry("800x600")
        
        self.product_manager = ProductManager()
        self.sale_manager = SaleManager()
        
        self.setup_ui()
    
    def setup_ui(self):
        # Menu principal
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)
        
        # Abas
        self.sales_tab = ttk.Frame(self.notebook)
        self.products_tab = ttk.Frame(self.notebook)
        self.reports_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.sales_tab, text="Vendas")
        self.notebook.add(self.products_tab, text="Produtos")
        self.notebook.add(self.reports_tab, text="Relatórios")
        
        self.setup_sales_tab()
        self.setup_products_tab()
        self.setup_reports_tab()
    
    def setup_sales_tab(self):
        # Lista de produtos na venda atual
        self.sales_tree = ttk.Treeview(self.sales_tab, columns=('ID', 'Produto', 'Qtd', 'Preço', 'Total'))
        self.sales_tree.heading('ID', text='ID')
        self.sales_tree.heading('Produto', text='Produto')
        self.sales_tree.heading('Qtd', text='Quantidade')
        self.sales_tree.heading('Preço', text='Preço')
        self.sales_tree.heading('Total', text='Total')
        self.sales_tree.pack(pady=10)
        
        # Campos para adicionar produto
        frame = ttk.Frame(self.sales_tab)
        frame.pack(pady=10)
        
        ttk.Label(frame, text="ID Produto:").grid(row=0, column=0)
        self.product_id_entry = ttk.Entry(frame)
        self.product_id_entry.grid(row=0, column=1)
        
        ttk.Label(frame, text="Quantidade:").grid(row=0, column=2)
        self.quantity_entry = ttk.Entry(frame)
        self.quantity_entry.grid(row=0, column=3)
        
        ttk.Button(frame, text="Adicionar Item", command=self.add_item_to_sale).grid(row=0, column=4, padx=5)
        ttk.Button(frame, text="Finalizar Venda", command=self.finish_sale).grid(row=0, column=5, padx=5)
    
    def setup_products_tab(self):
        # Lista de produtos
        self.products_tree = ttk.Treeview(self.products_tab, columns=('ID', 'Nome', 'Preço', 'Estoque'))
        self.products_tree.heading('ID', text='ID')
        self.products_tree.heading('Nome', text='Nome')
        self.products_tree.heading('Preço', text='Preço')
        self.products_tree.heading('Estoque', text='Estoque')
        self.products_tree.pack(pady=10)
        
        # Campos para adicionar produto
        frame = ttk.Frame(self.products_tab)
        frame.pack(pady=10)
        
        ttk.Label(frame, text="Nome:").grid(row=0, column=0)
        self.product_name_entry = ttk.Entry(frame)
        self.product_name_entry.grid(row=0, column=1)
        
        ttk.Label(frame, text="Preço:").grid(row=0, column=2)
        self.product_price_entry = ttk.Entry(frame)
        self.product_price_entry.grid(row=0, column=3)
        
        ttk.Label(frame, text="Estoque:").grid(row=0, column=4)
        self.product_stock_entry = ttk.Entry(frame)
        self.product_stock_entry.grid(row=0, column=5)
        
        ttk.Button(frame, text="Adicionar Produto", command=self.add_product).grid(row=0, column=6, padx=5)
        
        self.load_products()
    
    def setup_reports_tab(self):
        ttk.Button(self.reports_tab, text="Relatório de Vendas", command=self.show_sales_report).pack(pady=10)
        ttk.Button(self.reports_tab, text="Relatório de Estoque", command=self.show_stock_report).pack(pady=10)
    
    def add_product(self):
        name = self.product_name_entry.get()
        price = float(self.product_price_entry.get())
        stock = int(self.product_stock_entry.get())
        
        self.product_manager.add_product(name, price, stock)
        self.load_products()
        
        self.product_name_entry.delete(0, tk.END)
        self.product_price_entry.delete(0, tk.END)
        self.product_stock_entry.delete(0, tk.END)
    
    def load_products(self):
        for item in self.products_tree.get_children():
            self.products_tree.delete(item)
        
        for product in self.product_manager.get_all_products():
            self.products_tree.insert('', 'end', values=product)
    
    def add_item_to_sale(self):
        product_id = int(self.product_id_entry.get())
        quantity = int(self.quantity_entry.get())
        
        product = self.product_manager.get_product(product_id)
        if product:
            total = product[2] * quantity
            self.sales_tree.insert('', 'end', values=(product_id, product[1], quantity, product[2], total))
        
        self.product_id_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
    
    def finish_sale(self):
        items = []
        for item in self.sales_tree.get_children():
            values = self.sales_tree.item(item)['values']
            items.append((values[0], values[2]))  # (product_id, quantity)
        
        if items:
            sale_id = self.sale_manager.create_sale(items)
            messagebox.showinfo("Sucesso", f"Venda {sale_id} realizada com sucesso!")
            
            # Atualizar estoque
            for product_id, quantity in items:
                self.product_manager.update_stock(product_id, quantity)
            
            # Limpar lista de itens
            for item in self.sales_tree.get_children():
                self.sales_tree.delete(item)
            
            self.load_products()
    
    def show_sales_report(self):
        # Implementar relatório de vendas
        pass
    
    def show_stock_report(self):
        # Implementar relatório de estoque
        pass
    
    def run(self):
        self.root.mainloop()