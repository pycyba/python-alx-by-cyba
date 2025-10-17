# \w+ oznacza ciąg "znaków tworzących słowa", czyli: liter (także innych alfabetów), cyfr i znaku _
# findall znajduje wszystkie wystąpienia tego ciągu w linii tekstu
# żeby nie pisać ifa przy dostępie do słownika, użyjemy metody get z domyślną wartością 0
import re

slownik = {}
with open('pan_tadeusz.txt', mode='r', encoding='UTF-8') as wejscie:
    for linia in wejscie:
        slowa = re.findall(r'\w+', linia)
        for slowo in slowa:
            slownik[slowo] = slownik.get(slowo, 0) + 1

print('Łączna liczba słów:', sum(slownik.values()))
print('Liczba różnych słów:', len(slownik))
print('\nWszystkie słowa:')
for slowo, ile in sorted(slownik.items(), key=lambda t: t[1], reverse=True):
    print(f'{slowo} : {ile}')

