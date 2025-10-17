import pandas as pd

emps = pd.read_csv('emps.csv', sep=';')

szukany_job = input('Podaj nazwę stanowiska: ')

# Filtrowanie zwn warunek logiczny
wybrani = emps[emps.job_title == szukany_job]

print('Liczba pracowników:', len(wybrani))
if len(wybrani) > 0:
    print('Średnia pensja:', wybrani.salary.mean())
    print('Minimalna pensja:', wybrani.salary.min())
    print('Maksymalna pensja:', wybrani.salary.max())
