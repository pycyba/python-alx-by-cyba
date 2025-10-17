from emp import wczytaj

emps = wczytaj('emps.csv')
min_salary = 1000000000
# min_salary = float('+inf')
max_salary = 0
# max_salary = float('-inf')
min_employee = ''
max_employee = ''

for emp in emps:
    if emp.salary > max_salary:
        max_salary = emp.salary
        max_employee = emp.first_name + ' ' + emp.last_name
    if emp.salary < min_salary:
        min_salary = emp.salary
        min_employee = emp.first_name + ' ' + emp.last_name


print('Najbiedniejszy:', min_employee, min_salary)
print('Najbogatszy:', max_employee, max_salary)
