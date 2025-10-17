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

pattern1 = re.compile(r'([0-9]{4})-([0-9]{2})-([0-9]{2}) ([0-9]{2}:[0-9]{2}:[0-9]{2})')
pattern2 = re.compile(r'\w{3} (\w{3}) ([0-9]{2}) ([0-9]{2}:[0-9]{2}:[0-9]{2}) ([0-9]{4})')

months = {
    'Jan': '01',
    'Feb': '02',
    'Mar': '03',
    'Apr': '04',
    'May': '05',
    'Jun': '06',
    'Jul': '07',
    'Aug': '08',
    'Sep': '09',
    'Oct': '10',
    'Nov': '11',
    'Dec': '12',
}

with open('snapper.log', mode='r', encoding='UTF-8') as wejscie:
    for linia in wejscie:
        if match := pattern1.match(linia):
            print(f'1. data {match[3]}.{match[2]}.{match[1]}, godzina {match[4]}')
        elif match := pattern2.match(linia):
            print(f'2. data {match[2]}.{months[match[1]]}.{match[4]}, godzina {match[3]}')
        else:
            print('linia nie pasuje do żadnego wzorca')



