import pandas as pd

emps = pd.read_csv('emps.csv', sep=';', index_col=0)

for nr, emp in emps.iterrows():
    print(f'Pracownik {emp.first_name} {emp.last_name} zarabia {emp.salary}')

