"""
Użytkownik wprowadza napis
Program obliczam ile w tym tekście występuje samogłosek
(liter ze zbioru aeiouyąęó )
piękna pogoda → 6
"""

samogloski = {'a', 'e', 'i', 'o', 'u', 'y', 'ą', 'ę', 'ó'}
napis = input('Podaj napis:\n').lower()
ile = 0
for znak in napis:
    if znak in samogloski:
        ile += 1

print(ile)
