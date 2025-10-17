"""
Do pliku posortowany.txt zapisz wszystkie linie PT posortowane alfabetycznie.
Dla chętnych: pomijaj puste linie oraz usuwaj wcięcia lewej strony.
"""

print('odczyt')
with open('pan_tadeusz.txt', mode='r', encoding='UTF-8') as wejscie:
    linie = wejscie.readlines()

print('filtrowanie i sortowanie')
linie = sorted(linia.lstrip() for linia in linie if linia.strip())

print('zapis')
with open('posortowany.txt', mode='w', encoding='UTF-8') as wyjscie:
    wyjscie.writelines(linie)

print('gotowe')
