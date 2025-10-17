# Ta wersja nie jest optymalna pod względem wydajności.
# Dla każdego joba powtarzamy czytanie CAŁEJ listy prcowników.
from emp import wczytaj
emps = wczytaj('emps.csv')

# najpierw ustalamy, jakie są joby
jobs = {emp.job_title for emp in emps}
# print(jobs)

# dla każdego joba przeglądamy listę pracowników i liczymy średnią tych, którzy mają job_title równe job
for job in jobs:
    suma = 0
    ile = 0
    for emp in emps:
        if emp.job_title == job:
            suma += emp.salary
            ile += 1
    srednia = suma / ile
    print(f'{job:32} | {ile:2} | {srednia:8.2f}')
