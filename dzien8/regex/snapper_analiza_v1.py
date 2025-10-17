"""
Czytając linie z pliku snapper.log
za pomocą wyrażeń regularnych odczytaj z każdej linii datę i godzinę zdarzenia
biorąc pod uwagę, że data może być podana w jednym z dwóch formatów.
Niezależnie od formatu wypisz na wyjście informacje o dacie w jednolitym formacie
np. dd.mm.yyyy HH:MM:SS

Jeśli to ułatwi zadanie - możesz wypisać miesiąc słownie (Oct) lub liczbowo bez poprawiania
Ale jak dasz radę, to zamień tekst na liczbę za pomocą match albo słownika zamian.
Można też użyć funkcji związanych z formatowaniem dat z modułu datetime...
"""

import re

with open('snapper.log', mode='r', encoding='UTF-8') as wejscie:
    for linia in wejscie:
        match1 = re.match(r'([0-9]{4})-([0-9]{2})-([0-9]{2}) ([0-9]{2}:[0-9]{2}:[0-9]{2})', linia)
        match2 = re.match(r'\w{3} (\w{3}) ([0-9]{2}) ([0-9]{2}:[0-9]{2}:[0-9]{2}) ([0-9]{4})', linia)
        if match1:
            print(f'1. data {match1[3]}.{match1[2]}.{match1[1]}, godzina {match1[4]}')
        elif match2:
            print(f'2. data {match2[2]}.{match2[1]}.{match2[4]}, godzina {match2[3]}')
        else:
            print('linia nie pasuje do żadnego wzorca')



