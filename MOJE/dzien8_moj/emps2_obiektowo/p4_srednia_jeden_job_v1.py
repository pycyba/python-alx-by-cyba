# p4_srednia_jeden_job
from emp import wczytaj

emps = wczytaj('emps.csv')
job = input('Podaj nazwę stanowiska:\n')
suma = 0
ile = 0
for emp in emps:
    if emp.job_title == job:
        suma += emp.salary
        ile += 1

if ile > 0:
    srednia = suma / ile
    print(f'Na stanowisku {job} pracuje {ile} osób, a ich średnia pensja to {srednia:.2f}.')
else:
    print(f'Nikt nie pracuje na stanowisku {job}.')
