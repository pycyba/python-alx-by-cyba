"""
Wypisz na ekran wszystkie linie Pana Tadeusza ponumerowane rosnąco od 1
"""
# with open('pan_tadeusz.txt', mode='r', encoding='UTF-8') as wejscie:
#     nr = 0
#     for linia in wejscie:
#         nr += 1
#         print(nr, linia.rstrip()) # alternatywnie print(linia, end='')



# inny zapis:
with open('pan_tadeusz.txt', mode='r', encoding='UTF-8') as wejscie:
    for nr, linia in enumerate(wejscie, 1):
        print(nr, linia.rstrip())





"""
Ponumerowane linie PT zapisz do nowego pliku, np. 'ponumerowany.txt'
Przy okazji pomijaj linie, które są puste.
"""

with open('pan_tadeusz.txt', mode='r', encoding='UTF-8') as wejscie:
    with open('ponumerowany.txt', mode='w', encoding='UTF-8') as wyjscie:
        nr = 0
        for linia in wejscie:
            gola = linia.strip()
            if gola != '':
                nr += 1
                print(nr, gola, file=wyjscie)

print('Gotowe')


import time

"""
Ponumerowane linie PT zapisz do nowego pliku, np. 'ponumerowany.txt'
Przy okazji pomijaj linie, które są puste.
"""
t1 = time.time()

with open('pan_tadeusz.txt', mode='r', encoding='UTF-8') as wejscie,\
     open('ponumerowany.txt', mode='w', encoding='UTF-8') as wyjscie:
    for nr, linia in enumerate((linia for linia in wejscie if linia.strip()), 1):
        print(f'{nr:5}: {linia}', end='', file=wyjscie)

t2 = time.time()
print('Gotowe, czas wykonania:', t2-t1)


