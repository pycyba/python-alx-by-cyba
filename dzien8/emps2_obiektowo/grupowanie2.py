# Używając defaultdict zamiast dict, możemy uniknąć pisania ifów

from collections import defaultdict
from emp import wczytaj
emps = wczytaj('emps.csv')

sumy = defaultdict(float)
ilosci = defaultdict(int)

for emp in emps:
    sumy[emp.job_title] += emp.salary
    ilosci[emp.job_title] += 1

for job in sorted(sumy.keys()):
    suma = sumy[job]
    ile = ilosci[job]
    srednia = suma / ile
    print(f'{job:32} | {ile:2} | {srednia:8.2f}')
