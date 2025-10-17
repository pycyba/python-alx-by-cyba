import random

zakres = 10
rozmiar = 10
# Utwórz listę o rozmiarze `rozmiar` losowych liczb z zakresu od 1 do `zakres` włącznie

# lista = []
# for _ in range(rozmiar):
#     lista.append(random.randint(1, zakres))
# print(lista)

# podejście oparte o "comprehension"
lista = [random.randint(1, zakres) for _ in range(rozmiar)]
print(lista)

# Wypisz drugą co do wielkości liczbę w tej liście.
# Jeśli liczba, która jest największa, występuje dwa lub więcej razy,
# to wynikiem ma być następna co do wielkości.
# [20, 90, 80, 90, 70, 90] → wynikiem ma być 80

# rozwiązanie 1 - posortuj liczby bez powtórzeń i weź drugi największy element
s = sorted(set(lista))
print(s)

if len(s) > 1:
    print(s[-2])
else:
    print('muszę zagrać w lotto')

# koszt sortowania wynosi n log n

# tutaj wystarczy przejrzeć listę raz lub dwa razy i mieć drugą co do wielkosci liczbę
# gdyby naszym priorytetem była wydajność, to mamy jeszcze takie rozwiązania:
zbior = set(lista)
maks1 = max(zbior)
zbior.remove(maks1)
if len(zbior) > 0:
    maks2 = max(zbior)
    print('maks2:', maks2)
print()

# rozwiązanie "szkolne", w sam raz na programowanie w C albo Pascalu
# założenie - w liście nie ma elementów ujemnych
maks1 = maks2 = 0
for x in lista:
    if x > maks1:
        maks2 = maks1
        maks1 = x
    elif x > maks2 and x != maks1:
        maks2 = x

print('maks1:', maks1)
print('maks2:', maks2)


