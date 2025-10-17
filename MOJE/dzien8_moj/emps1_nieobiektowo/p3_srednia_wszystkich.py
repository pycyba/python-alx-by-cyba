""" p3_srednia_wszystkich
Program oblicza średnią pensję wszystkich pracowników
6461.68....
"""
with open('emps.csv', mode='r', encoding='UTF-8') as wejscie:
    wejscie.readline() # pomiń pierwszą linię
    suma = 0
    ile = 0
    for linia in wejscie:
        t = linia.strip().split(';')
        suma += int(t[4])
        ile += 1

    srednia = suma / ile
    print(f'W firmie pracuje {ile} osób, a ich średnia pensja to {srednia:.2f}')
    print(srednia)
