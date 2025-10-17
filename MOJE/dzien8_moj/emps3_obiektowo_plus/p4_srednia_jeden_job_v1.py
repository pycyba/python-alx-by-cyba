from employees import Employee

emps = Employee.read_csv('emps.csv')
jaki_job = input('Podaj nazwę stanowiska, np. Programmer: ')
ile = 0
suma = 0
for emp in emps:
    if emp.job_title == jaki_job:
        suma += emp.salary
        ile += 1

if ile > 0:
    srednia = suma / ile
    print(f'Średnia pensja {ile} pracowników na stanowisku {jaki_job} wynosi: {srednia:.2f}')
else:
    print(f'Nikt nie pracuje na stanowisku {jaki_job}')

