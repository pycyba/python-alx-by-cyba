from employees import Employee

emps = Employee.read_csv('emps.csv')
print('Liczba odczytanych rekordów:', len(emps))
for emp in emps:
    print(emp)
