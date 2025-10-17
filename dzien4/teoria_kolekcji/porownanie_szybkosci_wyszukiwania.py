from random import randint
from datetime import datetime

size = int(input('Podaj liczbę elementów: '))
limit = int(input('Podaj limit losowania: '))

# tworzę listę o rozmiarze size, która zawiera losowe elementy z zakresu od 1 do limit
czas1 = datetime.now()
lista = []
for _ in range(size):
    lista.append(randint(1, limit))
czas2 = datetime.now()

print('Lista gotowa. len=', len(lista))
print('Czas generowania:', czas2 - czas1)

print('Tworzenie zbioru na podstawie listy')
czas1 = datetime.now()
zbior = set(lista)
czas2 = datetime.now()
print('Zbiór gotowy. len=', len(zbior))
print('Czas generowania:', czas2 - czas1)
print()

while True:
    liczba = int(input('Podaj szukaną liczbę (-1 przerywa): '))
    if liczba < 0: break
    czas1 = datetime.now()
    inlist = liczba in lista
    czas2 = datetime.now()
    print(f'Element {"należy" if inlist else "nie należy"} do listy')
    print('Czas sprawdzania:', czas2 - czas1)
    czas1 = datetime.now()
    inset = liczba in zbior
    czas2 = datetime.now()
    print(f'Element {"należy" if inset else "nie należy"} do zbioru')
    print('Czas sprawdzania:', czas2 - czas1)

print('Koniec programu')
