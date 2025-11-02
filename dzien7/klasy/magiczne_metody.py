class Liczba:
    def __init__(self, wartosc):
        self.wartosc = wartosc

    def __str__(self):
        return f'Liczba o wartości {self.wartosc}'

    def __repr__(self):
        return f'Liczba({self.wartosc})'

    def __add__(self, other):
        return Liczba(self.wartosc + other.wartosc)
    # iadd +=

    def __sub__(self, other):
        return Liczba(self.wartosc - other.wartosc)

    def __mul__(self, other):
        return Liczba(self.wartosc * other.wartosc)

    def __truediv__(self, other):
        return Liczba(self.wartosc / other.wartosc)

    # truediv → /
    # floordiv → //
    # mod → %

    def __eq__(self, other): # ==
        return self.wartosc == other.wartosc

    def __lt__(self, other): # <
        return self.wartosc < other.wartosc

    def __le__(self, other): # <=
        return self.wartosc <= other.wartosc
    # wystarczy zaimplementować te trzy operatory,
    # a pozostałe trzy: ne, gt, ge zostaną automatycznie zdefiniowane na zasadzie negacji

    def __int__(self):
        return int(self.wartosc)

    def __float__(self):
        return float(self.wartosc)

    def __bool__(self):
        return self.wartosc != 0



a = Liczba(5)
b = Liczba(3)
zero = Liczba(0)

print('a:', a)
print('b:', b)
suma = a + b
print('suma:', suma)
print('iloczyn:', a*b)

print(a == a)
print(a == b)
print(a != b)
print(a < b)
print(a <= b)
print(a > b)
print(a <= b)

if a:
    print('a nie jest zerem')

if zero:
    print('zero nie jest zerem')
else:
    print('zero jest zerem')
