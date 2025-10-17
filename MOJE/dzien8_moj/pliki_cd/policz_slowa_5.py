# \w+ oznacza ciąg "znaków tworzących słowa", czyli: liter (także innych alfabetów), cyfr i znaku _
# findall znajduje wszystkie wystąpienia tego ciągu w tekście
# W tej wersji uruchamiamy findall na całej treści pliku - nie dzielimy pliku na linie.
# Zamiast słownika używamy klasy Counter.
# Wszystkie słowa zamieniamy na małe litery.
import re
from collections import Counter
import locale

with open('pan_tadeusz.txt', mode='r', encoding='UTF-8') as wejscie:
    cntr = Counter(re.findall(r'\w+', wejscie.read()))

print('Łączna liczba słów:', sum(cntr.values()))
print('Liczba różnych słów:', len(cntr))

locale.setlocale(locale.LC_COLLATE, 'pl_PL')
print('\nWszystkie słowa:')
for slowo, ile in sorted(cntr.items(), key=lambda t: locale.strxfrm(t[0])):
    print(f'{slowo} : {ile}')

