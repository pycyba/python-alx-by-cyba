"""
Użytkownik wprowadza napis
Program obliczam ile w tym tekście występuje samogłosek
(liter ze zbioru  aeiouyąęó )
piękna pogoda → 6
"""

napis = input('Podaj napis:\n')
ile = 0
for znak in napis:
    if znak == 'a' or znak == 'e' or znak == 'i' or znak == 'o' or znak == 'u' or znak == 'y':
        ile += 1

print(ile)
