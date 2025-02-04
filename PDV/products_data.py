

produtos = {
    "ALIMENTOS": {
        "Cereais": [
            ("Arroz Integral Premium", 12.99, 100),
            ("Arroz Branco 5kg", 22.90, 100),
            ("Feijão Carioca 1kg", 8.99, 100),
            ("Feijão Preto 1kg", 9.99, 100),
            ("Aveia em Flocos 500g", 6.99, 50),
            ("Quinoa 500g", 15.99, 30),
        ],
        "Laticínios": [
            ("Leite Integral 1L", 4.99, 100),
            ("Queijo Mussarela kg", 32.90, 50),
            ("Iogurte Natural 500g", 7.99, 40),
            ("Manteiga 200g", 9.99, 60),
            ("Requeijão 200g", 6.99, 45),
        ],
        "Padaria": [
            ("Pão Francês kg", 12.99, 50),
            ("Pão de Forma Integral", 8.99, 30),
            ("Bolo de Chocolate", 15.99, 20),
            ("Croissant", 4.99, 40),
        ]
    },
    
    "BEBIDAS": {
        "Não Alcoólicas": [
            ("Água Mineral 500ml", 2.50, 200),
            ("Refrigerante Cola 2L", 8.99, 100),
            ("Suco de Laranja 1L", 9.99, 50),
            ("Energético 473ml", 8.99, 80),
        ],
        "Alcoólicas": [
            ("Cerveja Premium 355ml", 4.99, 120),
            ("Vinho Tinto 750ml", 45.90, 30),
            ("Vodka 750ml", 35.90, 25),
            ("Whisky 750ml", 89.90, 20),
        ]
    },

    "HIGIENE": {
        "Pessoal": [
            ("Sabonete 90g", 2.99, 150),
            ("Shampoo 400ml", 12.99, 80),
            ("Pasta de Dente 90g", 4.99, 100),
            ("Papel Higiênico 12un", 15.99, 60),
        ],
        "Limpeza": [
            ("Detergente 500ml", 3.99, 120),
            ("Sabão em Pó 1kg", 12.99, 80),
            ("Desinfetante 1L", 8.99, 90),
            ("Água Sanitária 1L", 4.99, 100),
        ]
    }
}

# Script para adicionar os produtos ao banco de dados
def populate_database():
    from product_manager import ProductManager
    pm = ProductManager()
    
    for categoria_principal, subcategorias in produtos.items():
        for subcategoria, items in subcategorias.items():
            for nome, preco, estoque in items:
                nome_completo = f"{categoria_principal} - {subcategoria} - {nome}"
                try:
                    pm.add_product(nome_completo, preco, estoque)
                    print(f"Adicionado: {nome_completo}")
                except Exception as e:
                    print(f"Erro ao adicionar {nome_completo}: {e}")

if __name__ == "__main__":
    populate_database()