# W tej wersji zamiast dwóch słowników będę używał jednego.
# Słownik będzie zawierał pary wartości (w formie dwuelementowej listy)
# 0 → liczba rekordów
# 1 → suma pensji

from emp import wczytaj
emps = wczytaj('emps.csv')

slownik = {}

for emp in emps:
    if emp.job_title in slownik:
        # aktualizacja danych
        slownik[emp.job_title][0] += 1
        slownik[emp.job_title][1] += emp.salary
    else:
        # nowy wpis
        slownik[emp.job_title] = [1, emp.salary]

# to działa:
# for job in slownik:
#     wpis = slownik[job]
#     ile = wpis[0]
#     suma = wpis[1]
#     srednia = suma / ile
#     print(f'{job:32} | {ile:2} | {srednia:8.2f}')

# ale to jest bardziej 'pajtoniczne':
for job, [ile, suma] in slownik.items():
    srednia = suma / ile
    print(f'{job:32} | {ile:2} | {srednia:8.2f}')
