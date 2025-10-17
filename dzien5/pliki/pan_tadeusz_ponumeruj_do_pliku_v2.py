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
