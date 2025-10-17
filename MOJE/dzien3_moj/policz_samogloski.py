"""
Użytkownik wprowadza napis
Program obliczam ile w tym tekście występuje samogłosek
(liter ze zbioru  aeiouyąęó )
"""

samogloski = {'a', 'e', 'i', 'o', 'u', 'y', 'ą', 'ę', 'ó'}
tekst = str(input("Podaj tekst: ")).lower()
ilosc_samoglosek = 0
for znak in tekst:
    if znak in samogloski:
        ilosc_samoglosek += 1

print(ilosc_samoglosek)
