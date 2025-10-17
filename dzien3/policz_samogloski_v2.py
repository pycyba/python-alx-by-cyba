"""
Użytkownik wprowadza napis
Program obliczam ile w tym tekście występuje samogłosek
(liter ze zbioru  aeiouyąęó )
piękna pogoda → 6
"""

napis = input('Podaj napis:\n').lower()
ile = 0
for znak in napis:
    if znak in 'aeiouyąęó':
        ile += 1

print(ile)
