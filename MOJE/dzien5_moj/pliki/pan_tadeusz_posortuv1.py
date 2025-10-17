"""
Do pliku posortowany.txt zapisz wszystkie linie PT posortowane alfabetycznie.
Dla chętnych: pomijaj puste linie oraz usuwaj wcięcia lewej strony.
"""

print('odczyt')
with open('pan_tadeusz.txt', mode='r', encoding='UTF-8') as wejscie:
    linie = wejscie.readlines()

print('filtrowanie')
linie2 = []
for linia in linie:
    if linia.strip():
        linie2.append(linia.lstrip())

print('sortowanie')
linie2.sort()

print('zapis')
with open('posortowany.txt', mode='w', encoding='UTF-8') as wyjscie:
    wyjscie.writelines(linie2)

print('gotowe')
