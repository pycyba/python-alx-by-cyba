# p2_wypisz_bogatych - wypisz tylko tych pracowników, którzy zarabiają ≥ 10 tys

from emp import wczytaj

emps = wczytaj('emps.csv')
for emp in emps:
    if emp.salary >= 10_000:
        print(emp)
