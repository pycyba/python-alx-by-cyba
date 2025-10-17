import re

razem = 0
with open('pan_tadeusz.txt', mode='r', encoding='UTF-8') as wejscie:
    for linia in wejscie:
        # slowa = re.split(r'\s+', linia)
        slowa = re.split(r'[\s,.—;:()!?«»…]+', linia)
        for slowo in slowa:
            if slowo:
                print(slowo)
                razem += 1

print('Łączna liczba słów:', razem)
