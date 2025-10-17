from collections import defaultdict
from statistics import mean

from emp import wczytaj
emps = wczytaj('emps.csv')

# Troche inne podejście - tworzymy słownik, który zawiera listy obiektów Employee.
# Grupowanie w znaczenu dosłownym, a nie tak jak w SQL.
slownik = defaultdict(list)
for emp in emps:
    slownik[emp.job_title].append(emp)

# mamy teraz możliwość wypisać elementy podzielone na grupy:
for job, lista in slownik.items():
    print(f'Pracownicy ze stanowiska {job} ({len(lista)} elementów):')
    for emp in lista:
        print(' * ', emp)
    print(f'Średnia pensja: {mean(emp.salary for emp in lista)}')
    print()
