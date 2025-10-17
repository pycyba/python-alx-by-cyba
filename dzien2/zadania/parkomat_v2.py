# w tej wersji skracamy zapis, stosujemy odejmowanie zamiast dodawania

cena = 4
czas = int(input('Podaj liczbę godzin parkowania: '))
do_zaplaty = cena * czas
print(f'Za {czas} godzin płacisz {do_zaplaty}')

while do_zaplaty > 0:
    print(f'Pozostało {do_zaplaty}')
    do_zaplaty -= int(input('wrzuć monetę: '))

if do_zaplaty < 0:
    print(f'Wydaję {-do_zaplaty} reszty i gotowe')
else:
    print('Wpłacono ile trzeba :)')
