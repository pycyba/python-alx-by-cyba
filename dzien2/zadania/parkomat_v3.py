cena = 4
czas = int(input('Podaj liczbę godzin parkowania: '))
do_zaplaty = cena * czas
print(f'Za {czas} godzin płacisz {do_zaplaty}')

poprawne_monety = {1, 2, 5}

suma_wplat = 0
while suma_wplat < do_zaplaty:
    print(f'Wpłacono {suma_wplat}, pozostało {do_zaplaty-suma_wplat}')
    try:
        moneta = int(input('wrzuć monetę: '))
        if moneta not in poprawne_monety:
            print('Niepoprawna moneta')
            continue
        suma_wplat += moneta
    except ValueError:
        print('Niepoprawny format liczby')

if suma_wplat > do_zaplaty:
    reszta = suma_wplat - do_zaplaty
    print(f'Wydaję {reszta} reszty')

print('Do widzenia')
