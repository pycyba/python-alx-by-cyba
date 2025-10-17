import csv

with open('emps.csv', mode='r', encoding='utf-8') as input:
    reader = csv.reader(input, delimiter=';')

    next(reader) # aby pominąć pierwszy wiersz, w którym są nagłówki
    for emp in reader:
        print(f'Pracownik {emp[1]} {emp[2]} ({emp[3]}) zarabia {emp[4]} USD')
