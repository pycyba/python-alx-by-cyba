from employees import read_csv

emps = read_csv('emps.csv')

for emp in emps:
    print(f'Pracownik {emp.first_name} {emp.last_name} ({emp.job_title}) zarabia {emp.salary} USD')
    print(f'Employee  {emp[1]} {emp[2]} ({emp[3]}) earns ${emp[4]}')
    # modyfikacja zabroniona: emp.first_name = 'Jan'

# Dla obiektów namedtuple możliwy jest dostęp dol pól poprzez nazwę atrybutu oraz przez numer pozycji
