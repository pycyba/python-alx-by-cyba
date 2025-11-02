"""
Zaimplementuj klasę Vector dostarczającą funkcjonalność wektora
swobodnego na dwuwymiarowej płaszczyźnie. Wektory powinny
mieć możliwość dodawania, odejmowania, mnożenia (przez liczbę),
porównywania (po długości) oraz powinny posiadać czytelną
reprezentację napisową.

Przykład użycia:
vector_1 = Vector(x=1, y=2)
vector_2 = Vector(1, 2)
vector_7 = Vector(7, 5)
vector_3 = vector_1 + vector_2
vector_m = vector2 * 10
"""

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({repr(self.x)}, {repr(self.y)})'

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    # wersja z porównywaniem obu współrzędnych
    # def __eq__(self, other):
    #     return self.x == other.x and self.y == other.y

    # dekorator @property powoduje, że aby odczytać wynik tej metody, nie używa się już wywołania
    # v.dlugosc()
    # tylko stosuje się zapis taki jak przy odczycie atrybutu (zmiennej)
    # v.dlugosc
    @property
    def dlugosc(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    # wersja z porównywaniem długości
    def __eq__(self, other):
        return self.dlugosc == other.dlugosc

    def __lt__(self, other):
        return self.dlugosc < other.dlugosc

    def __le__(self, other):
        return self.dlugosc <= other.dlugosc

    # rzutowanie na wartości True/False, aby móc pisać np
    # if wektor: ...
    # Wektor zerowy jest fałszem,
    # a niezerowy (przynajmniej jedna współrzędna różna od zera) jest prawdą
    def __bool__(self):
        return self.x != 0 or self.y != 0

    # odczyt zawartości poprzez kwadratowe nawiasy
    # np. wektor[0] powinno dać wartość współrzędnej x
    # ale pozwalam też na wektor['x']
    def __getitem__(self, item):
        match item:
            case 0 | 'x' | 'X' : return self.x
            case 1 | 'y' | 'Y' : return self.y
            case _: raise KeyError(item)

def main():
    a = Vector(5, 3)
    b = Vector(2, 2)
    c = Vector(-5, 2.5)
    z = Vector()
    print(a, b, c, z)
    print(repr(c))
    print(a+b)
    print(a-b)
    print(b-a)

    print(a[0], a[1], a['x'], a['y'])

    print(a * 5) # 25, 15
    print(5 * b)

    print(a.dlugosc)
    print(z.dlugosc)

    print(a == b)
    print(b == c)
    print(a != b)
    print()

    print(a < b)
    print(a <= b)
    print(a > b)
    print(a >= b)
    if b:
        print('b nie jest zerem')

    if not z:
        print('z jest zerem')

if __name__ == '__main__':
    main()
