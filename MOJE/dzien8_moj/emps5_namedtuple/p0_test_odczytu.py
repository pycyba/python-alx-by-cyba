from employees import read_csv

emps = read_csv('emps.csv')
print('Liczba odczytanych rekordów:', len(emps))
for emp in emps:
    print(emp)
