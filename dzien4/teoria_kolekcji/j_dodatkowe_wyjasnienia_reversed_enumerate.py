lista = ['Ala', 'Basia', 'Celina', 'Dorota']
print('lista:', lista)

# funkcja reversed zwraca taki specjalny obiekt, który tylko daje dostęp do listy w odwróconej kolejności
# ale to nie jest kopia dznych (z tego wynika, że działa to wydajnie)
rev = reversed(lista)
print(rev, 'obiekt typu:', type(rev))

# aby dostać się do elementów, możemy użyć pętli for lub wielokrotnie funkcji next
for e in rev:
    print(e, end='; ')
print()
# przy okazji - próba kolejnej iteracji po elementach już nie działa - brak kolejnych elementów
for e in rev:
    print(e, end='; ')
print()

# można też utworzyć listę na podstawie wyniku reversed
odwrocona = list(reversed(lista))
print('odwrocona:', odwrocona)
# oryginalna lista nie została odwrócona
print('lista:', lista)
print()

# Natomiast metoda reverse odwraca elementy wewnątrz listy
# zawartość listy ulega zmianie, ale sama metoda nie zwraca żadnego wyniku
lista.reverse()
print('lista.reverse()')
print('lista:', lista)

# Gdybym próbował pobrać wynik reverse(), to dostałbym None
wynik = lista.reverse()
print('wynik reverse:', wynik)
print('lista:', lista)
print()

lista.extend(['Łukasz', 'Ula', 'Marek', 'Piotr', 'Ewelina', 'Żaneta', 'Ćma'])
import random
random.shuffle(lista)
print(lista)

# Analogicznie do reverse / reversed, mamy do dyspozycji dwie operacja sortowania
# sorted(kolekcja) - zwraca nową listę zawierająca posortowane elementy, ale nie modyfikuje przekazanej kolekcji
# lista.sort() - sortuje zawartość listy (modyfikuje obiekt listy), a nie zwraca wyniku (None)

posortowana = sorted(lista)
print('posortowana:', posortowana)
print('lista:', lista)

wynik = lista.sort()
print('lista.sort(), wynik =', wynik)
print('lista:', lista)

# Kolejny problem - jak posortować napisy uwzględniając kolejność alfabetu polskiego?
import locale
locale.setlocale(locale.LC_COLLATE, 'pl_PL') # albo '' co oznacza aktualne ustawienia komputera
# wciąż sort i sorted sortowałyby wg kodów Unicode, czyli ąęźż lądują na końcu
# ale gdy teraz użyjemy specjalnej funkcji strxfrm, to już posortuje po polsku
lista.sort(key=locale.strxfrm)
print('lista:', lista)
print()

wynik = enumerate(lista)
print('enumerate zwraca obiekt', wynik, 'typu', type(wynik))
# obiekt daje dstęp do elementów listy wraz z ich numerami
# w pętli for możemy przejrzeć to, co zwraca enumerate:
for entry in wynik:
    print(entry)
    print('   numer:', entry[0], 'wartość:', entry[1])
print()

# W praktyce z enumerate korzysta się tak,
# stosując technikę "rozpakowywania"
for i, imie in enumerate(lista):
    print(f'Osoba nr {i} ma na imię {imie}.')
