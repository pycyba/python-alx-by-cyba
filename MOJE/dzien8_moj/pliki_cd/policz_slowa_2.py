import re
slownik = {}
razem = 0
with open('pan_tadeusz.txt', mode='r', encoding='UTF-8') as wejscie:
    for linia in wejscie:
        # slowa = re.split(r'\s+', linia)
        slowa = re.split(r'[\s,.—;:()!?«»…]+', linia)
        for slowo in slowa:
            if slowo:
                slownik[slowo] = slownik.get(slowo, 0) + 1
                razem += 1

print('Łączna liczba słów:', razem)

for slowo in slownik.keys():
    print(slowo, slownik[slowo])