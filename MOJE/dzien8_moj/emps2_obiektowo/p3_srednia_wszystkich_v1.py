# p3_srednia_wszystkich
from emp import wczytaj

emps = wczytaj('emps.csv')
suma = 0
for emp in emps:
    suma += emp.salary
ile = len(emps)

srednia = suma / ile
print(f'W firmie pracuje {ile} osób, a ich średnia pensja to {srednia:.2f}')
