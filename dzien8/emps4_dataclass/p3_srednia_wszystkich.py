from employees import Employee

emps = Employee.read_csv('emps.csv')
suma = 0
for emp in emps:
    suma += emp.salary

srednia = suma / len(emps)
print('Średnia wszystkich:', srednia)
