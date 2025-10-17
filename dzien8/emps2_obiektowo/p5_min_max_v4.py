from emp import wczytaj

emps = wczytaj('emps.csv')
min_employee = min(emps, key=lambda emp: emp.salary)
max_employee = max(emps, key=lambda emp: emp.salary)

print('Najbiedniejszy:', min_employee)
print('Najbogatszy:', max_employee)
