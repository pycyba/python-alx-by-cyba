"""
Wersja rozbudowana:
Program w pętli prosi o podawanie nazw produktów i ich ilości
a na końcu podaje łączną sumę do zapłaty.
Można przyjąć np., że program kończy się, gdy użytkownik wciśnie enter
zamiast podawać nazwę kolejnego towaru. (wtedy input zwraca pusty napis '')
Zadbaj o to, aby podanie nieznanego towaru nie przerwało programu, tylko wypisz jakiś komunikat.
"""
cennik = {
    'woda': 3.90,
    'kawa': 12.50,
    'herbata': 14.40,
    'mleko': 4.40,
}

print(cennik)

suma = 0
while True:
    towar = input('Podaj nazwę towaru: ')
    if towar == '':
        break
    ile = int(input('Podaj liczbę sztuk: '))
    do_zaplaty = cennik[towar] * ile
    suma += do_zaplaty
    print(f'Za {ile} sztuk towaru {towar} płacisz {do_zaplaty:.2f}. Wartość koszyka {suma:.2f}.')

print(f'Koniec zakupów. Łącznie do zapłaty {suma:.2f}.')

