"""
Zadanie:
zapytaj użytkownika o nazwę towaru oraz liczbę sztuk
i wypisz ile jest do zapłaty zgodnie z cennikiem.
"""

cennik = {
    'woda': 3.90,
    'kawa': 12.50,
    'herbata': 14.40,
    'mleko': 4.40,
}

towar = input('Podaj nazwę towaru: ')
ile = int(input('Podaj liczbę sztuk: '))
do_zaplaty = cennik[towar] * ile
print('Do zapłaty', do_zaplaty)
