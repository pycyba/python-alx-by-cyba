# Program pozwala uruchomić wybraną funkcję dla podanego parametru.
# Podaje wynik i zmierzony czas działania.

from datetime import datetime
from funkcje_liczbowe import *

def koniec_programu(kod):
    print('No to nara...')
    exit(kod)


FUNKCJE = [
    koniec_programu,
    suma_cyfr_v1,
    suma_cyfr_v2,
    suma_cyfr_v3,
    suma_cyfr_v4,
    silnia_rek,
    silnia,
    fib_rek,
    fib_tab,
    fib,
    najmniejszy_dzielnik,
    czy_pierwsza_1,
    czy_pierwsza_2,
    czy_pierwsza_3,
    czy_pierwsza_4,
    czy_pierwsza_5,
]


def wypisz_funkcje():
    print('Program uruchomi wybraną funkcję, gdy podasz jej numer z listy oraz argument.')
    print('Funkcja numer 0 z argumentem 0 kończy program.')
    print('\nFunkcje do wyboru:')
    for nr, f in enumerate(FUNKCJE):
        print(f'{nr:3} → {f.__name__}')


def main():
    wypisz_funkcje()
    while True:
        try:
            nr = int(input('\nPodaj numer funkcji: '))
            f = FUNKCJE[nr]
            x = int(input('Podaj argument (liczbę naturalną): '))
            if x < 0:
                raise ValueError('Liczba ujemna')
            pocz = datetime.now()
            wynik = f(x)
            konc = datetime.now()
            print('Wynik:', wynik)
            print('Czas wykonania:', konc - pocz)
        except Exception as e:
            print('Błąd', e)


if __name__ == '__main__':
    main()
