import csv

with open('emps.csv', mode='r', encoding='utf-8') as input:
    reader = csv.DictReader(input, delimiter=';')

    # dict reader czyta każdy rekord jako słownik, gdzie kluczami są nazwy kolumn
    # pierwszy wiersz automatycznie jest pomijany - biblioteka zakłada, że są w nim nazwy kolumn
    # 'a la JSON'
    for emp in reader:
        print(f'Pracownik {emp["first_name"]} {emp["last_name"]} ({emp["job_title"]}) zarabia {emp["salary"]} USD')
