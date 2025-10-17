class Liczba:
    def __init__(self, wartosc):
        self.wartosc = wartosc
    def __str__(self):
        return f'Wartosc: {self.wartosc}'
    def __add__(self, other):
        return Liczba(self.wartosc + other.wartosc)
    def __mul__(self, other):
        return Liczba(self.wartosc * other.wartosc)
a = Liczba(100)
b = Liczba(200)

suma = a + b
