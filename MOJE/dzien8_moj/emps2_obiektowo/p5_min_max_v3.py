from emp import wczytaj

emps = wczytaj('emps.csv')
min_employee = emps[0]
max_employee = emps[0]

for emp in emps:
    if emp.salary > max_employee.salary:
        max_employee = emp
    if emp.salary < min_employee.salary:
        min_employee = emp

print('Najbiedniejszy:', min_employee)
print('Najbogatszy:', max_employee)
