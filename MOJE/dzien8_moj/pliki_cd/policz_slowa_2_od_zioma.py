# W tej wersji plik dzielimy na słowa za pomocą re.split (każdą linię oddzielnie)
# Słowa liczymy w oparciu o słownik, w którym zapamiętujemy słowo z 1, gdy pojawia się po raz pierwszy
# a zwiększamy o 1, gdy pojawia się po raz kolejny.

import re

slownik = {}
with open('pan_tadeusz.txt', mode='r', encoding='UTF-8') as wejscie:
    for linia in wejscie:
        slowa = re.split(r'[\s,.—;:()!?«»…*]+', linia)
        for slowo in slowa:
            if slowo in slownik:
                slownik[slowo] += 1
            else:
                slownik[slowo] = 1

# usuwam puste słowo:
del slownik['']

print('Łączna liczba słów:', sum(slownik.values()))
print('Liczba różnych słów:', len(slownik))
print('\nWszystkie słowa:')
for slowo, ile in slownik.items():
    print(f'{slowo} : {ile}')

