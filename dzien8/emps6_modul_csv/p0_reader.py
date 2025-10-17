import csv

with open('emps.csv', mode='r', encoding='utf-8') as input:
    reader = csv.reader(input, delimiter=';')
    print(reader)
    # reader jest iteratorem, który dostarcza kolejnych rekordów, przy czym pierwszy jest tworzony na podstawie wiersza nagłówkowego

    # odczytuję nazwy kolumn:
    headers = next(reader)
    print('Nazwy kolumn:', headers)

    # dalej są wiersze z danymi - każdy zostanie odczytany jako lista
    for emp in reader:
        print(emp)
