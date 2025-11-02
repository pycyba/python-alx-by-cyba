import pandas

emps = pandas.read_csv('emps.csv', sep=';', parse_dates=['hire_date'])

kolumna_grupowania = input('Podaj nazwę kolumny grupowania: ')
kolumna_statystyk = input('Podaj nazwę kolumny do liczenia statystyk: ')
funkcja = input('Podaj nazwę funkcji: ')

wynik = emps.groupby(kolumna_grupowania)[kolumna_statystyk].agg(funkcja)

print(wynik)

