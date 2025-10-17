from emp import wczytaj

# Teraz w programie cały proces wczytania danych z pliku sprowadza się do jednej linii.
emps = wczytaj('emps.csv')
print(f'Wczytano {len(emps)} rekordów.')

# W tej wersji wypisujemy rekordy w taki sposób, jaki jest przygotowany w metodzie __str__
for emp in emps:
    print(emp)
