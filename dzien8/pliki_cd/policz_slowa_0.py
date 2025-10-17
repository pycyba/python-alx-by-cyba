razem = 0
with open('pan_tadeusz.txt', mode='r', encoding='UTF-8') as wejscie:
    for linia in wejscie:
        slowa = linia.split()
        for slowo in slowa:
            print(slowo)
            razem += 1

print('Łączna liczba słów:', razem)
