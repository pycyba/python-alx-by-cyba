# Pętla to jest konstrukcja, która umożliwia wielokrotne wykonanie fragmentu kodu.

# Zamiast pisać
print('Ala ma kota')
print('Ala ma kota')
print('Ala ma kota')
print()

# można za pomocą pętli kazać powtórzyć linię kodu wiele razy
for i in range(5):
    print('Ola ma psa')
print()

# W Pythonie istnieją dwa rodzaje pętli: while i for
# while WARUNEK: INSTRUKCJE
# Jeśli WARUNEK prawdziwy → wykonywane są INSTRUKCJE, a następnie ponownie sprawdzany WARUNEK itd
# Jeśli WARUNEK fałszywy → INSTRUKCJE są pomijane, a program idzie dalej

# while 2+2 == 4:
#     print('matematyka działa')

# UWAGA - to jest prosty przykład szkoleniowy, ale normalnie takie rzeczy w Pythonie realizuje się pętla for i in range
x = 1
while x < 5:
    print(x)
    x += 1 # x=x+1

print('Pętla while zakończona. Teraz x ==', x)

# Pętli while używa się raczej wtedy, gdy:
# a) piszemy pętlę nieskończoną lub pętlę przyrywaną za pomocą break
# wtedy wpiszemy while True: .....
# b) mamy bardziej skomplikowane warunki

napis = 'Ala ma kota'
while len(napis) < 100:
    print(napis)
    napis += ' i innego kota'

print('Finalny napis:\n', napis)
print('Długość:', len(napis))
print()

# for ZMIENNA in ŹRÓDŁO_DANYCH: INSTRUKCJE
# Python pobiera po jednym elemencie z podanego źródła,
# wpisuje ten element do ZMIENNEJ i wykonuje INSTRUKCJE
# Zazwyczaj INSTRUKCJE korzystają ze ZMIENNEJ

# Źródłem danych mogą być:
# - listy i inne kolekcje
miasta = ['Warszawa', 'Kraków', 'Wrocław', 'Łódź', 'Poznań']
for m in miasta:
    print('Pozdrawiamy miasto', m)
print()

# - range - generator liczb całkowitych z określonego zakresu
# ogólny zapis range(start, stop, step)
# co generuje wartości od `start` włącznie do `stop` wyłączając, z krokiem `step`
for i in range(100, 150, 10):
    print(i)
print()

# gdy są tylko dwa parametry, to są to start i stop, a step jest równy 1
for liczba in range(20, 30):
    print(liczba, end=', ')
print()
print()

# gdy jest tylko jeden parametr, to za start uznaje się 0
for i in range(5):
    print(i)

# ogólnie rzecz biorąc źródłem dla nych dla for może być dowolny "obiekt iterowalny" - zostanie to wyjaśnione pod koniec kursu w temacie "iteratory i generatory"
# praktyczne zastosowania: odczyt danych z plików, baz danych, przeglądanie struktur związanych z obliczeniami naukowymi i analizą danych
