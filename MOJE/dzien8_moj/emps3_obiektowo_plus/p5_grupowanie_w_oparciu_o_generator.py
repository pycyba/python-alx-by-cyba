from employees import Employee

emps = Employee.read_csv_generator('emps.csv')
print(emps) # generator
slownik = {}
# W słowniku kluczem jest job, a wartością jest dwuelementowa lista: [count, sum]

for emp in emps:
    if emp.job_title in slownik:
        slownik[emp.job_title][0] += 1
        slownik[emp.job_title][1] += emp.salary
    else:
        slownik[emp.job_title] = [1, emp.salary]

# dwupoziomowe rozpakowanie - dane lądują od razu w zmiennych
for job, (ilosc, suma) in slownik.items():
    srednia = suma / ilosc
    print(f'| {job:32} | {ilosc:2} | {srednia:8.2f} |')
