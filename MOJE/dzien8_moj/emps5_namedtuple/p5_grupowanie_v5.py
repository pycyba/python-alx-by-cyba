from collections import defaultdict
from employees import read_csv

emps = read_csv('emps.csv')
# Jako parametr defaultdict wpisuje się "przepis na nowy element".
# Gdy podajemy przykładowo int, to używane jest to w taki sposób, że jest wywoływane int() , a to daje wynik 0.
# Tutaj podamy funkcję, która nie pobiera argumentów, a wyniku zwraca nową listę zaweirającą dwa zera.
slownik = defaultdict(lambda: [0, 0])

for emp in emps:
    slownik[emp.job_title][0] += 1
    slownik[emp.job_title][1] += emp.salary

print(slownik)
print()

for job, (ilosc, suma) in slownik.items():
    srednia = suma / ilosc
    print(f'| {job:32} | {ilosc:2} | {srednia:8.2f} |')
