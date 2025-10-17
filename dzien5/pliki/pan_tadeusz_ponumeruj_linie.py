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
