"""
Program odczytuje dwie liczby - długości boków prostokąta.
Program oblicza pole powierzchni oraz obwód prostokąta.
"""

# na zasadzie: "zobaczcie, jakie bajery są w Pythonie"
a, b = map(float, input('Podaj dwie liczby (boki prostokąta) rozdzielając spacją:\n').split())

pole = a * b
obw = 2*a + 2*b
# f-string to wygodny sposób umieszczania wyliczonych wartości wewnątrz tekstów
print(f'Prostokąt o bokach {a} i {b} ma pole równe {pole} a obwód równy {obw}')
print(f'Prostokąt o bokach {a} i {b} ma pole równe {pole:.1f} a obwód równy {obw:.1f}')
