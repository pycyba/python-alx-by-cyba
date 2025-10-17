# Iteratory są podstawą działania pętli for w Pythonie. Wytłumaczymy po kolei...

# Iteratorem jest obiekt, na którym Python może wywołać metodę __next__
# Ten iterator dostarcza liczb nieparzystych od 1 do podanego limitu włącznie.
class IteratorNieparzystych:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    # Metoda __next__ powina zwtócić "następny element" dostarczany przez ten iterator.
    # Przygotowujemy się na to, że ta metoda będzie wielokrotnie wywoływana w pętli.
    # Aby poinformować, że wszystkie elementy zostały zwrócone i następnych już nie będzie, metoda powinna zgłosić wyjątek StopIteration.
    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        wynik = self.current
        self.current += 2
        return wynik


# W Pythonie istnieje wbudowana funkcja next, która działa tak, że wywołuje wbudowaną metodę __next__
it = IteratorNieparzystych(5)
x = next(it) # wewnętrznie działa it.__next__()
print('pierwszy wynik:', x)
x = next(it)
print('drugi wynik:', x)
x = next(it)
print('trzeci wynik:', x)
try:
    x = next(it)
    print('czwarty wynik:', x)
except StopIteration:
    print('Koniec iteracji')
print(40*'=' + '\n')

# Obiekt iterowalny (iterable) to taki obiekt, który posiada metodę __iter__, za pomocą której pobiera się iterator.

class IterableNieparzystych:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        return IteratorNieparzystych(self.limit)

    def __str__(self):
        return f'Potrafię zwrócić iterator liczb od 1 do {self.limit}'


obiekt = IterableNieparzystych(9)
print(obiekt)
# właśnie takie obiekty "iterowalne" można w Pythonie przekazywać do pętli for
for i in obiekt:
    print(f'{i=}')
print()
# Inaczej niż same iteratory, obiekty iterowalne mogą być używane wielokrotnie w pętli:
for i in obiekt:
    print(f'{i=}')
print()

# Wewnętrznie KAŻDA PĘTLA FOR w Pythonie działa tak:
# 1) z przekazanego obiektu iterowalnego pobierany jest iterator za pomocą __iter__
# 2) w pętli wielokrotnie wywoływane jest next, aż do pojawienia się wyjątku StopIteration
print('Początek pętli A')
it = obiekt.__iter__()
try:
    while(True):
        j = it.__next__()
        print(f'{j=}')
except StopIteration:
    pass
print('Koniec pętli A\n')

# Można to też zapisać używając funkcji globalnych iter() i next()
print('Początek pętli B')
it = iter(obiekt)
try:
    while(True):
        k = next(it)
        print(f'{k=}')
except StopIteration:
    pass
print('Koniec pętli B')
