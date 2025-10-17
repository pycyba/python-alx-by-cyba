def osoby():
    yield 'Ala'
    yield 'Ela'
    print('funkcja: jestem między Elą a Olą')
    yield 'Ola'


print('Zdefiniowałem funkcję:', osoby)
# Funkcja, które w swojej treści zawiera instrukcję yield zwraca w wyniku "obiekt generatora"
gen = osoby()
print(gen)

# I dopiero wywołując na tym obiekcie metodę next() lub wstawiając go do pętli for
# uzyskamy wartości, które ta funkcja zwraca poleceniem yield.
try:
    a = next(gen)
    print('wynik1:', a)
    a = next(gen)
    print('wynik2:', a)
    a = next(gen)
    print('wynik3:', a)
    a = next(gen)
    print('wynik4:', a)
except StopIteration:
    print('StopIteration')
print()

# W praktyce elementy z generatora zwykle uzyskuje się w pętli for
for o in osoby():
    print('Kolejna osoba:', o)
print()

lista = list(osoby())
print('lista osób:', lista)
