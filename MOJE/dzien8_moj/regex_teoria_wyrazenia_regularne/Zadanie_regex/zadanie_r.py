"""
Czytając linie z pliku snapper.log
za pomocą wyrażeń regularnych odczytaj z każdej linii datę i godzinę zdarzenia
biorąc pod uwagę, że data może być podana w jednym z dwóch formatów.
Niezależnie od formatu wypisz na wyjście informacje o dacie w jednolitym formacie
np. dd.mm.yyyy HH:MM:SS
Jeśli to ułatwi zadanie - możesz wypisać miesiąc słownie (Oct) lub liczbowo bez poprawiania
Ale jak dasz radę do zamień tekst na liczbę za pomocą match albo słownika zamian.
"""

import re

pattern1 = re.compile(r'([0-9]{4})-([0-9]{2})-([0-9]{2})\s+([0-9]{2}:[0-9]{2}:[0-9]{2})')
pattern2 = re.compile(r'\w+\s+(\w+)\s+(\d+)\s+([0-9]{2}:[0-9]{2}:[0-9]{2})\s+([0-9]{4})')

MONTHS = {
    'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
    'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12',
}


with open('snapper.log', mode='r', encoding='UTF-8') as plik:
    for linia in plik:
        m1 = pattern1.search(linia)
        m2 = pattern2.search(linia)
        if m1:
            print(f'{m1.group(3)}.{m1.group(2)}.{m1.group(1)} {m1.group(4)}')
        elif m2:
            print(f'{m2.group(2)}.{MONTHS[m2.group(1)]}.{m2.group(4)} {m2.group(3)}')






