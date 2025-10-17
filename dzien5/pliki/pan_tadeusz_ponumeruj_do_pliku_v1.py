import time

"""
Ponumerowane linie PT zapisz do nowego pliku, np. 'ponumerowany.txt'
Przy okazji pomijaj linie, które są puste.
"""
t1 = time.time()
with open('pan_tadeusz.txt', mode='r', encoding='UTF-8') as wejscie:
    with open('ponumerowany.txt', mode='w', encoding='UTF-8') as wyjscie:
        nr = 0
        for linia in wejscie:
            gola = linia.strip()
            if gola != '':
                nr += 1
                print(nr, gola, file=wyjscie)

t2 = time.time()
print('Gotowe, czas wykonania:', t2-t1)
