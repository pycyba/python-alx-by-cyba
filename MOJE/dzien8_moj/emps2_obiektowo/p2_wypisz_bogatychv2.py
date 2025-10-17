# p2_wypisz_bogatych - wypisz tylko tych pracowników, którzy zarabiają ≥ 10 tys

from emp import wczytaj

bogaci = [f'{emp.first_name} {emp.last_name}' for emp in wczytaj('emps.csv') if emp.salary >= 10_000]
print('\n'.join(bogaci))
