# \w+ oznacza ciąg "znaków tworzących słowa", czyli: liter (także innych alfabetów), cyfr i znaku _
# findall znajduje wszystkie wystąpienia tego ciągu w tekście
# W tej wersji uruchamiamy findall na całej treści pliku - nie dzielimy pliku na linie.
# Jako słownika używamy defaultdict, dzięki czemu nie musimy sprawdzać ifem, czy słowo występowało wcześniej.
# Wszystkie słowa zamieniamy na małe litery.
import re
from collections import defaultdict

slownik = defaultdict(int)

with open('pan_tadeusz.txt', mode='r', encoding='UTF-8') as wejscie:
    tresc = wejscie.read()
    slowa = re.findall(r'\w+', tresc)
    for slowo in slowa:
        slownik[slowo.lower()] += 1

print('Łączna liczba słów:', sum(slownik.values()))
print('Liczba różnych słów:', len(slownik))
print('\nWszystkie słowa:')
for slowo, ile in sorted(slownik.items(), key=lambda t: t[1], reverse=True):
    print(f'{slowo} : {ile}')

