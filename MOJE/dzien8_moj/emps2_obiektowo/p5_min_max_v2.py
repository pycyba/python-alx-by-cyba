from emp import wczytaj

emps = wczytaj('emps.csv')
min_employee = None
max_employee = None

for emp in emps:
    if min_employee is None or emp.salary < min_employee.salary:
        min_employee = emp
    if max_employee is None or emp.salary > max_employee.salary:
        max_employee = emp

print('Najbiedniejszy:', min_employee)
print('Najbogatszy:', max_employee)
