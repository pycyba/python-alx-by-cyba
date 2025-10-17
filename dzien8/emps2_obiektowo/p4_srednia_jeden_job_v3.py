from emp import wczytaj
from statistics import mean, StatisticsError

emps = wczytaj('emps.csv')
job = input('Podaj nazwę stanowiska:\n')

try:
    srednia = mean(emp.salary for emp in emps if emp.job_title == job)
    print(srednia)
except StatisticsError as e:
    print(e)
