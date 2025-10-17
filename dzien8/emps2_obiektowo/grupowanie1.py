# Cel: dla każdego job_title obliczyć średnią pensję pracowników na tym stanowisku
# To rozwiązanie oparte o słowniki ma dobrą wydajność.

from emp import wczytaj
emps = wczytaj('emps.csv')

sumy = {}
ilosci = {}

for emp in emps:
    if emp.job_title in sumy:
        # jeśli to jest kolejny pracownik o takim job_title, to dodajemy pensję do sumy
        sumy[emp.job_title] += emp.salary
        ilosci[emp.job_title] += 1
    else:
        # jeśli pierwszy pracownik z danego job_title, to tworzymy nowy wpis w słowniku
        sumy[emp.job_title] = emp.salary
        ilosci[emp.job_title] = 1

for job in sumy.keys():
    suma = sumy[job]
    ile = ilosci[job]
    srednia = suma / ile
    print(f'{job:32} | {ile:2} | {srednia:8.2f}')
