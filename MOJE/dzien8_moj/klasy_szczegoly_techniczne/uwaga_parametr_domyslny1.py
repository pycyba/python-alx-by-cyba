import random

def dopisz_i_wypisz(n, lista=[]):
    # do przekazanej listy dopisuje losową wartość i wypisuje całą listę
    # domyślnie lista jest pusta
    # przy takim zapisie wszystkie ywołania funkcji, w któyrch nie podaje się drugiego arguemntu, będą korzystać z tego samego obiektu lista
    for i in range(n):
        lista.append(random.randint(1, 100))
    print(lista)



dopisz_i_wypisz(1, [5, 10, 15])
dopisz_i_wypisz(3, [11, 12, 13, 14, 15])

dopisz_i_wypisz(5)
dopisz_i_wypisz(2)
dopisz_i_wypisz(1, [100, 200])
dopisz_i_wypisz(3)
print(30 * '=')

# rozwiązanie poprawne, aby za każdym razem powstała pusta lista:
def dopisz_i_wypisz2(n, lista=None):
    # do przekazanej listy dopisuje losową wartość i wypisuje całą listę
    # domyślnie lista jest pusta
    if lista is None:
        lista = []
    for i in range(n):
        lista.append(random.randint(1, 100))
    print(lista)


dopisz_i_wypisz2(5)
dopisz_i_wypisz2(2)
dopisz_i_wypisz2(1, [100, 200])
dopisz_i_wypisz2(3)