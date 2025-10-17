jedno_imie = 'Alicja'

# Lista
lista_imion = ['Ala', 'Ola', 'Ula', 'Andrzej', 'Ala', 'Tadeusz']
lista_liczb = [100, 105, 110, 125, 200, 0, -50]
miks = [300, 'napis', 3.14, "inny napis", [5, 10, 15]]

print(type(jedno_imie), type(lista_imion), type(lista_imion[1]))
print(lista_imion)
print(lista_liczb)
print(miks)
print()
print(lista_imion[1])
print(miks[4][1])
# jbc w numpy istnieją tablice wielowymiarowe
# i dostęp do elementu z wiersza nr 5, kolumny nr 3
# wyglądałby tak:
# tablica[5,3]

# próba dostępu do elementu spoza zakresu kończy się błędem
#ERR print(lista_imion[5])
# Indeks ujemny oznacza liczenie od końca. -1 to ostatni element
print(lista_imion[-1])
# działa to na zasadzie len-pozycja:
print(lista_imion[len(lista_imion)-1])
print()

# zakresy, 'slicing'
print(lista_imion[1:4])
print(lista_imion[:3])
print(lista_imion[1:5:2])
print(lista_imion[::2])
print(lista_imion[::-1])
print()

napis = '_ABCDEFGH'
print(napis[2:5])
print(napis[:5])
print(napis[::-1])
print()

# Dla wszystkich kolekcji, w tym dla list, można stosować pętlę for
for imie in lista_imion:
    print('Witaj', imie)
    plik = open(f'{imie}.txt', mode='w')
    print(f'Hej {imie}!', file=plik)
    plik.close()

# listy można modyfikować (listy są 'mutowalne')
# wpisanie innej wartości na określoną pozycję:
print(lista_imion, lista_liczb)
lista_imion[1] = 'Aleksandra'
lista_liczb[0] += 1
print(lista_imion, lista_liczb)

# Metody służące do dodawania elementów
lista_imion.append('Łukasz')
lista_imion.insert(1, 'Ela')
lista_imion.extend(['Zuzia', 'Kasia', 'Patryk'])
# zadziałałoby też lista_imion += ['Zuzia', 'Kasia', 'Patryk']
print(lista_imion)

# dwie wersje operacji sortowania:
# sorted(lista albo coś innego) – zwraca w wyniku NOWĄ posortowaną listę
imiona_posortowane = sorted(lista_imion)
print('posortowane:', imiona_posortowane)
print('oryginalne:', lista_imion)

# .sort() - metoda, która zmiena kolejność wewnątrz listy
lista_liczb.sort(reverse=True)
print(lista_liczb)
print()

# usuwanie elementów
ostatni = lista_imion.pop()
print('Pobrano', ostatni)
del lista_imion[2]
lista_imion.remove('Andrzej') # usuwa pierwsze wystąpienie
print(lista_imion)
# lista utworzona wcześniej za pomocą sorted wciąż ma wszystkie elementy
print('posortowane:', imiona_posortowane)
print()

# zbiór (set)
# element w zbiorze nie powtarzają się

zbior = {'Warszawa', 'Kraków', 'Gdańsk', 'Kraków'}
print(zbior, 'rozmiar:', len(zbior))
# dla zbioru nie ma operacji odczytywania elementu z pozycji
# print(zbior[1])
# operacją, która ma największy sens, jest sprawdzenie, czy coś do zbioru należy, czy nie
if 'Łódź' in zbior:
    print('Łódź jest')
else:
    print('Łodzi nie ma')
print()

# Dodaj element do zbioru - operacja add
zbior.add('Wrocław')
zbior.add('Poznań')
zbior.add('Szczecin')
zbior.add('Kraków')
print(zbior)

# usuwanie za pomocą remove
zbior.remove('Szczecin')
print(zbior)

# Można przejrzeć wszystkie elementy za pomocą for
for miasto in zbior:
    print(f'Pozdrawiamy {miasto}')

# Pusty zbiór tworzy się za pomocą set() a nie {}
# Łatwo utworzyć zbiór na podstaiwe listy i odwrotnie
print(set(lista_imion))
print()

# dla zbiorów dostępne są operacje
# | → suma zbiorów
# & → przecięcie / część wspólna zbioru
# - → różnica zbiorów
# ^ → od sumy odejmujemy część wspólną

# słownik - dict
# słownik przechowuje pary   klucz: wartość

cennik = {'kawa': 9, 'woda': 4, 'cola': 8, 'soczek': 8}
sale = {404: 'Python', 401: 'PowerPoint', 403: 'Linux'}
# też ok : sale = {404: 'Python', 401: ['PowerPoint', 'Word', 'Excel'], 403: 'Linux'}
print(cennik)
print(sale)

print('liczba towarów w cenniku:', len(cennik))

# odczyt wartości spod określonego klucza
print('cena coli:', cennik['cola'])
print('szkolenie w naszej sali:', sale[404])
print()

towar = 'kawa'
if towar in cennik:
    print(f'Towar {towar} istnieje i ma cenę {cennik[towar]}')
else:
    print(f'Towar {towar} jest nieznany')



