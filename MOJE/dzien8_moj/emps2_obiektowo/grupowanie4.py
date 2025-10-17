from collections import defaultdict
from emp import wczytaj
emps = wczytaj('emps.csv')

# To, co przekazuje się do defaultdict, to jest "przepis na nowy element".
# To ma być funkcja, której użyje defaultdict w razie braku danych.
# Nawet, gdy piszemy int czy list, to nie jest to traktowane jak nazwa typu,
# tylko jak funkcja. Np. int() daje wynik 0
slownik = defaultdict(lambda: [0, 0])

for emp in emps:
        slownik[emp.job_title][0] += 1
        slownik[emp.job_title][1] += emp.salary

for job, [ile, suma] in slownik.items():
    srednia = suma / ile
    print(f'{job:32} | {ile:2} | {srednia:8.2f}')
