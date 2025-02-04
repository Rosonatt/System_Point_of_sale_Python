# main.py
from config import create_database
from products_data import populate_database
from main_window import MainWindow

if __name__ == "__main__":
    create_database()
    populate_database()
    app = MainWindow()
    app.run()