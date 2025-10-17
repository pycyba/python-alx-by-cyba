"""
Napisz program zliczający liczbę znaków w podanym przez
użytkownika napisie pomiędzy nawiasami <>.

Ala ma <kota>, a kot ma Alę
4
"""

napis = input('Podaj napis:\n')

# rozwiązanie oparte o pętlę i zapamiętywanie 'stanu'
wynik = 0
liczymy = False
for znak in napis:
    if znak == '<':
        liczymy = True
    elif znak == '>':
        liczymy = False
    elif liczymy:
        wynik += 1
print(wynik)

# rozwiązania oparte o znajdowanie pozycji:
p = napis.find('<')
k = napis.find('>')
# alternatywnie można było użyć .index('<')
fragment = napis[p+1:k]
print(fragment)
print(len(fragment))

# jeśli nie potrzebujemy fragmentu, tylko długości, to wystarczy matematyczne odejmowanie
print(k-p-1)

# tylko jako ciekawostka, rozwiązanie z regexpami
import re
znajdy = re.findall(r'<([^>]*)>', napis)
print(znajdy)
print(sum(len(s) for s in znajdy))
