"""
Zaimplementuj klasę Product przechowującą informację o cenie,
nazwie oraz ID produktu. Zaimplementuj metodę wypisującą
informację o produkcie na konsolę.

Przykład użycia:
product = Product(1, 'Woda', 10.99)
product.print_info()
Produkt "Woda", id: 1, cena: 10.99 PLN
"""

class Product:
    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        print(f'Produkt "{self.nazwa}", id: {self.id}, cena: {self.cena} PLN')


product = Product(1, 'Woda', 10.99)
product.print_info()

mleko = Product(2, 'mleko', 2.90)
mleko.print_info()
