"""
Do pliku posortowany.txt zapisz wszystkie linie PT posortowane alfabetycznie.
Dla chętnych: pomijaj puste linie oraz usuwaj wcięcia lewej strony.

W tej wersji stosujemy techniki, które zagwarantują sortowanie zgodne z polskim alfabetem.
"""

import locale

print('odczyt')
with open('pan_tadeusz.txt', mode='r', encoding='UTF-8') as wejscie:
    linie = wejscie.readlines()

print('filtrowanie i sortowanie')
locale.setlocale(locale.LC_COLLATE, 'pl_PL')
# locale.setlocale(locale.LC_COLLATE, 'Polish')
# locale.setlocale(locale.LC_COLLATE, 'fr_CA')
# locale.setlocale(locale.LC_COLLATE, 'en_US')
# wywołanie z pustym stringiem ustawi język na podstawie konfiguracji systemowej
# locale.setlocale(locale.LC_COLLATE, '')
# to tylko eksperyment: locale.setlocale(locale.LC_CTYPE, 'pl_PL')

linie = sorted((linia.lstrip() for linia in linie if linia.strip()), key=locale.strxfrm)
# linie = sorted((linia.lstrip() for linia in linie if linia.strip()), key=len, reverse=True)
# również do sort można przekazać sort:
# linie.sort(key=locale.strxfrm)

print('zapis')
with open('posortowany.txt', mode='w', encoding='UTF-8') as wyjscie:
    wyjscie.writelines(linie)

print('gotowe')
