"""
Parkowanie kosztuje 4 zł za godzinę.
Program pyta o liczbę godzin
oblicza kwotę do zapłaty
i w pętli pobiera kolejne wpłaty (tak jakby monety, ale to po prostu liczby wczytywane inputem)
tak długo, aż zostanie wpłacona wymagana suma.
Jeśli okaże się, że wpłacono zbyt dużo, to automat "wydaje resztę" (wypisuje liczbę).
"""

cena = 4
czas = int(input('Podaj liczbę godzin parkowania: '))
do_zaplaty = cena * czas
print(f'Za {czas} godzin płacisz {do_zaplaty}')

suma_wplat = 0
while suma_wplat < do_zaplaty:
    print(f'Wpłacono {suma_wplat}, pozostało {do_zaplaty-suma_wplat}')
    moneta = int(input('wrzuć monetę: '))
    suma_wplat = suma_wplat + moneta

if suma_wplat > do_zaplaty:
    reszta = suma_wplat - do_zaplaty
    print(f'Wydaję {reszta} reszty')

print('Do widzenia')
