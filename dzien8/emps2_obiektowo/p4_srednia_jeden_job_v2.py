from emp import wczytaj

emps = wczytaj('emps.csv')
job = input('Podaj nazwę stanowiska:\n')

pensje = [emp.salary for emp in emps if emp.job_title == job]
if pensje:
    srednia = sum(pensje) / len(pensje)
    print(f'Na stanowisku {job} pracuje {len(pensje)} osób, a ich średnia pensja to {srednia:.2f}.')
else:
    print(f'Nikt nie pracuje na stanowisku {job}.')
