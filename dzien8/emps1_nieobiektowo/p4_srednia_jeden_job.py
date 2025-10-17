""" p4_srednia_jeden_job
Użytkownik podaje nazwę stanowiska np. Programmer
a program podaje lciczbę pracowników na takim stanowisku oraz ich średnią pensję
"""

job = input('Podaj nazwę stanowiska:\n')
suma = 0
ile = 0

with open('emps.csv', mode='r', encoding='UTF-8') as wejscie:
    wejscie.readline() # pomiń pierwszą linię
    for linia in wejscie:
        t = linia.strip().split(';')
        if t[3] == job:
            suma += int(t[4])
            ile += 1

if ile > 0:
    srednia = suma / ile
    print(f'Na stanowisku {job} pracuje {ile} osób, a ich średnia pensja to {srednia:.2f}.')
else:
    print(f'Nikt nie pracuje na stanowisku {job}.')
