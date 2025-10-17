class Liczba:
    def __init__(self, wartosc):
        self.wartosc = wartosc

    def __str__(self):
        return f'Liczba o wartości {self.wartosc}'

    def __add__(self, other):
        return Liczba(self.wartosc + other.wartosc)

    def __mul__(self, other):
        return Liczba(10 * self.wartosc + other.wartosc)


a = Liczba(5)
b = Liczba(3)

print('a:', a)
print('b:', b)
suma = a + b
print('suma:', suma)
print('iloczyn:', a*b)


