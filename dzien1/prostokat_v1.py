"""
Program odczytuje dwie liczby - długości boków prostokąta.
Program oblicza pole powierzchni oraz obwód prostokąta.
"""

a = float(input('Podaj pierwszy bok prostokąta: '))
b = float(input('Podaj drugi bok prostokąta: '))

pole = a * b
obw = 2*a + 2*b

print('pole:', pole)
print('obwód:', obw)
