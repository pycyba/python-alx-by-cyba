class PudelkoZapalek:
    def __init__(self, liczba_sztuk):
        self.liczba_sztuk = liczba_sztuk

    # Metoda __str__ ma za zadanie zwrócić tekstową reprezentację obiektu
    # taką, która będzie używana podczas rzutowania na string czy podczas printowania.
    def __str__(self):
        return '<' + self.liczba_sztuk * '|' + '>'

    # Metoda __repr__ ma zwrócić tekstową postać obiektu
    # ale przeznaczoną nie do czytania przez ludzi,
    # ale taką, która po wklejeniu do źródeł Pythona stworzy obiekt o takiej samej zawartości.
    def __repr__(self):
        return f'PudelkoZapalek({self.liczba_sztuk})'

    def __add__(self, other):
        return PudelkoZapalek(self.liczba_sztuk + other.liczba_sztuk)

    def __sub__(self, other):
        return PudelkoZapalek(self.liczba_sztuk - other.liczba_sztuk)
    # arytmetyka: add, sub, mul, mod, pow
    # dla dzielenia dwie wersje:
    # // floordiv
    #  / truediv

    # porównania: eq ne lt le gt ge
    # domyślnie eq, czyli ==, działa tak samo jak is, czyli sprawdza, 'czy to ten sam obiekt'
    # ale można to zmienić na wersję, która porównuje wartości pól
    def __eq__(self, other):
        return self.liczba_sztuk == other.liczba_sztuk

    def __lt__(self, other):
        return self.liczba_sztuk < other.liczba_sztuk

    def __le__(self, other):
        return self.liczba_sztuk <= other.liczba_sztuk

    # ne (!=) jest zdefiniowane jako zaprzeczenie eq i w praktyce ne się nie definiuje
    # również gt i ge są zdefiniowane jako negacje le i lt, też można nie definiować

    # rzutowania na standardowe typy Pythona
    def __bool__(self):
        return self.liczba_sztuk > 0

    def __int__(self):
        return self.liczba_sztuk


a = PudelkoZapalek(5)
b = PudelkoZapalek(3)
c = PudelkoZapalek(2)
r = c
z = PudelkoZapalek(0)

print('a:', a)
print('b:', b)
print('e:', z)
print('repr(a):', repr(a))
print('str(a):', str(a))
print()

suma = a + b
print('a+b:', suma, 'typu', type(suma))
print('a-b:', a-b)
print()

d = a-b
print('c:', c)
print('d:', d)
print('c == d', c == d)
print('c is d', c is d)
print('r:', r)
print('c == r', c == r)
print('c is r', c is r)
print()

print('a == b', a == b)
print('a != b', a != b)
print('a <  b', a <  b)
print('a <= b', a <= b)
print('a >  b', a >  b)
print('a >= b', a >= b)
print()

if a:
    print('pudełko nie jest puste')
else:
    print('puste pudełko')

print('int:', int(a))


