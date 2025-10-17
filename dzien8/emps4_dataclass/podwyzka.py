from employees import Employee

emps = Employee.read_csv('emps.csv')

job = input('Podaj nazwę stanowiska: ')
podwyzka = int(input('Podaj kwotę podwyżki: '))

for emp in emps:
    if emp.job_title == job:
        # emp.salary += podwyzka
        emp.zmien_pensje(podwyzka)

Employee.write_csv(emps, 'zmienione.csv')
print('Gotowe')
