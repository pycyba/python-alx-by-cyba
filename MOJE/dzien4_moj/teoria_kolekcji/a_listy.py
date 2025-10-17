# Listy są mutowalne (można je zmieniać)
# Listy pamiętają kolejność elementów i można indeksować (listy są sekwencjami)
# Listy mogą zawierać powtórzone wartości

imiona = ['Ala', 'Adam', 'Iwo\tna', 'Kasia', 'Ala', 'Janusz']
liczby = [0, 10, 20, 30, 40, 50, 60, 70, 80, 98]
miks = [123, 'Ala', 3.14, [3,2,1]]

print(imiona)
print(*imiona)
print(liczby)

print('Liczba imion:', len(imiona))
print('Liczba liczb:', len(liczby))
print('len(miks):', len(miks))

# de facto to jest wywołanie takiej metody, ale "zwykły programista" powinien używać funkcji len() aby to uzyskać
print('_len:', imiona.__len__())
print()

# A tak tworzy się pustą listę (2 sposoby)
pusta1 = []
pusta2 = list()

print(pusta1, len(pusta1), type(pusta1))
print()

# Łatwo można przejrzeć wszystkie elementy lista i dla każdego coś zrobić
for imie in imiona:
    print('Kolejną osobą jest', imie)
print()

for x in liczby:
    print(x, end='; ')
print()

# W przypadku kolekcji zawierająch liczby, można skorzystać z gotowych funkcji:
print('Suma:', sum(liczby))
print('Min:', min(liczby))
print('Max:', max(liczby))

# Po zaimportowaniu modułu statistics uzyskujemy dostęp
# do większej liczby funkcji statystycznych
import statistics
print('Średnia:', statistics.mean(liczby))
print('Mediana:', statistics.median(liczby))

# max i min dla dowolnych typów, które da się porównywać
print('Maksymalne imię:', max(imiona))
print()

# Odczytać konkretny element listy wg jego pozycji można za pomocą [indeksowania]
print(imiona[2])
# Obowiązuje numeracja od 0

# Można uzywać indeksów ujemnych - wtedy liczymy od końca.
# -1 to ostatni element
print(imiona[-1])

# Gdy wyjdziemy poza zakres listy ( >= rozmiar  albo < -rozmiar), to będzie wyjątek IndexError
#ERR print(imiona[10])
print()

# Listy są mutowalne - zawartość list można modyfikować.

# Zmiana elementu na określonej pozycji:
print(imiona)
imiona[0] = 'Alicja'
imiona[3] = 'Katarzyna'
# ale nie da się w ten sposób wpisać na nieistniejącą pozycję
#ERR imiona[6] = 'Alojzy'
print(imiona)

liczby[-1] += 1
print(liczby)

# Dodanie nowego elementu na końcu:
imiona.append('Krzysztof')
print(imiona)

# Wstawienie elementu w środek. Na pozycję 3 wstaw wartość Magdalena → reszta się przesunie
imiona.insert(3, 'Magdalena')
print(imiona)

# Aby za jednym zamachem dodać wiele elementów, można uzyć extend
inna_lista = ['Zuzia', 'Adrian', 'Bożena', 'Zuzia', 'Janusz']
# imiona.append(inna_lista)
# byłaby lista w liście: ['Alicja', 'Adam', 'Iwona', 'Magdalena', 'Katarzyna', 'Janusz', 'Krzysztof', ['Zuzia', 'Adrian', 'Bożena', 'Janusz']] rozmiar: 8

imiona.extend(inna_lista) # różnoważne imiona += inna_lista
# 4 dodatkowe imiona dodane na końcu listy
# ['Alicja', 'Adam', 'Iwona', 'Magdalena', 'Katarzyna', 'Janusz', 'Krzysztof', 'Zuzia', 'Adrian', 'Bożena', 'Janusz'] rozmiar: 11
print(imiona, 'rozmiar:', len(imiona))
print()

# Listy można też dodawać za pomocą + , ale to działa podobnie jak + w matematyce
a = [1,2,3]
b = [4,5]

print('a:', a, 'b:', b)
print('3 * a:', 3 * a)
print('a + b:', a + b)
# Listy a i b nadal pozostały sobą
print('a:', a, 'b:', b)
c = a + b
print('c:', c)

# Aby w ten sposób zmodyfikować istniejącą listę, można użyć
a += b
print('+=')
print('a:', a, 'b:', b)
# efekt analogiczny do extend

print()
# Usunięcie elementu z określonej pozycji. Dalsze elementy przesuwają się ← w lewo
print(imiona)
del imiona[1]
print(imiona)

# Usunięcie pierwszego znalezionego elementu o podanej wartości
imiona.remove('Janusz')
print(imiona)

# jakiś sposób, aby uzyskać listę bez wystąpień podanej wartości
# to tworzy nową listę bez Januszów, a oryginał się nie zmienia
#imiona = [imie for imie in imiona if imie != 'Janusz']

# inny sposób - usuwanie z tej listy do ostatniego wystąpienia
# wersja bardziej kosztowna:
# while 'Janusz' in imiona:
#     imiona.remove('Janusz')

# wersja mniej kosztowna:
# try:
#     while True:
#         imiona.remove('Janusz')
# except ValueError:
#     pass

# Próba usunięcia elementu niesitniejącego kończy się błędem
# imiona.remove('Mikołaj')
# print(imiona)
print()

# Aby sprawdzić, czy lista coś zawiera, używamy operatora in
# Przy czym dla listy jest to kosztowne - Python musi przejrzeć całą listę
if 'Iwona' in imiona:
    print('Lista zawiera imię Iwona')
else:
    print('Lista nie zawiera imienia Iwona')

if 'Katarzyna' in imiona:
    print('Lista zawiera imię Katarzyna')
else:
    print('Lista nie zawiera imienia Katarzyna')
print()

print(imiona)

# Spr. czy element należy do listy
print('Katarzyna' in imiona)
kogoszukam = 'Zuzia'
if kogoszukam in imiona:
    print('Znaleziono')
else:
    print('Nie ma')

# Metoda .count informuje, ile razy dana wartość jest zawarta w liście.
print(f'Element {kogoszukam} występuje {imiona.count(kogoszukam)} razy.')

# Jeśli interesuje nas nie tylko czy obiekt należy do listy, ale także na jakiej pozycji się znajduje, używamy wtedy metody index
pozycja = imiona.index(kogoszukam)
print(f'Osoba {kogoszukam} znajduje się na pozycji {pozycja}')
# Wywołanie index dla elementu, którego nie ma w liście, kończy się wyjątkiem

# pozycja = imiona.index('Patryk')

# 2 sposoby, żeby sobie z tym poradzić:
# Podejście "defensywne"
kogoszukam = 'Patryk'
if kogoszukam in imiona:
    pozycja = imiona.index(kogoszukam)
    print(f'Osoba {kogoszukam} znajduje się na pozycji {pozycja}')
else:
    print(f'Lista nie zawiera elementu {kogoszukam}')

# Podejście "ofensywne" - dość często praktykowane w Pythonie
# tym bardziej, że tutaj jest to ozwiązanie bardziej wydajne (tylko przeglądamy listę)
try:
    print(f'Osoba {kogoszukam} znajduje się na pozycji {imiona.index(kogoszukam)}')
except ValueError:
    print(f'Lista nie zawiera elementu {kogoszukam}')
print()

# Odwrócenie listy
print(liczby)
liczby.reverse()
print(liczby)

liczby.extend([33, 66, 99, 155])
print(liczby)

# Posortowanie listy
liczby.sort()
print(liczby)

print()

# Gdy korzysta się z listy jako "stosu", wtedy bardziej czytelne może być używanie operacji append i pop
l = []
l.append('Warszawa')
l.append('Kraków')
l.append('Łódź')
l.append('Wrocław')
l.append('Poznań')
print(l)
# pop usuwa ostatni element
print('3 razy pop() : ')
print(l.pop())
print(l.pop())
print(l.pop())
print(l)
l.append('Bydgoszcz')
l.append('Toruń')
print(l)
print()


# Zwykła pętla for przegląda elementy listy, nie mamy informacji o pozycji
for imie in imiona:
    print(imie)
print()

# Pętla w stylu języka C przeglądająca indeksy, w Pythonie wygląda tak:
for i in range(len(imiona)):
    print(f'{i} → {imiona[i]}')
print()

# Rozwiązaniem bezpośrednio służącym do przejrzenia elementów listy wraz z ich pozycjami, jest enumerate
# enumerate zwraca kolekcję par, czyli tupli.
# gdyby nie używać rozpakowywania, to byłoby tak:
for para in enumerate(imiona):
    print(para, 'typu', type(para))
print()

for para in enumerate(imiona):
    print(f'{para[0]} - {para[1]}')
print()

# Ale w praktyce zawsze używa się tu "rozpakowywania" (unpacking)
# czyli wpisuje się te dwie rzeczy na oddzielne zmienne
for i, imie in enumerate(imiona):
    print(f'{i} => {imie}')
print()

# Samo enumerate tworzy kolekcję par:
print(enumerate(imiona))
print(list(enumerate(imiona)))
# enumerate domyślnie numeruje od 0, ale można podać inny numer początkowy
print(list(enumerate(imiona, 11)))
print()

# Operacja zip na podstawie dwóch list tworzy listę par.
# Typowe zastosowanie to pętla przechodząca jednocześnie po dwóch listach.
lista1 = ['Opel', 'Toyota', 'BMW', 'Audi', 'VW', 'Fiat']
lista2 = ['Astra', 'Auris', 'X5', 'A6', 'Passat TDI']

for a, b in zip(lista1, lista2):
    # print(a, b)
    print(f'marka {a} model {b}')
print()

# Samo zip tworzy listę par:
zipped = zip(lista1, lista2)
print(zipped)
print(list(zipped))

slownik = dict(zip(lista1, lista2))
print(slownik)

# Jeszcze więcej "ułatwiaczy dostępu" w module itertools
print('Koniec programu')
