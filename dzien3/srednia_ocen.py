oceny = [5, 4, 2, 5, 1, 4, 3, 5]
print(oceny)
# Zadanie: oblicz średnią tych ocen
# Wypisz też info ile jest jedynek, ile jest szóstek

# Podejście ogólne, korzystamy tylko z podstawowych technik programowania
suma = 0
ile = 0
ile_1 = 0
ile_6 = 0
for ocena in oceny:
    suma += ocena
    ile += 1
    if ocena == 1: ile_1 += 1
    if ocena == 6: ile_6 += 1

print('suma:', suma)
srednia = suma / ile
print('średnia:', srednia)
print('liczba jedynek:', ile_1, ', liczba szóstek:', ile_6)
print()

# Podejścia uproszczone dzięki dodatkowym funkcjom Pythona...
srednia = sum(oceny) / len(oceny)
print('średnia:', srednia)
print('liczba jedynek:', oceny.count(1), ', liczba szóstek:', oceny.count(6))
print()

import statistics
srednia = statistics.mean(oceny)
print('średnia:', srednia)

from collections import Counter
podsumowanie = Counter(oceny)
print(podsumowanie)

for element, ile_razy in sorted(podsumowanie.items()):
    print(f'Ocena {element} występuje {ile_razy} razy')
