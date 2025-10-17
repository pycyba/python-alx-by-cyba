import pandas as pd

emps = pd.read_csv('emps.csv', sep=';')
print(emps)
print()

print('Ogólne statystyki pensji:\n', emps["salary"].describe())
#albo  print('Ogólne statystyki pensji:\n', emps.salary.describe())

print('Średnia wszystkich:', emps.salary.mean())

print('Unikalne nazwy miast:', list(emps.city.unique()))
