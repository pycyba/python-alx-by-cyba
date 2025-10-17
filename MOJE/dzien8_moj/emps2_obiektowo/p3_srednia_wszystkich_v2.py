from emp import wczytaj

emps = wczytaj('emps.csv')
srednia = sum(emp.salary for emp in emps) / len(emps)
print(srednia)

from statistics import mean
print(mean(emp.salary for emp in emps))
