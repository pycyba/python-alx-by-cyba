from employees import read_csv

emps = read_csv('emps.csv')

for emp in emps:
    print(f'Pracownik {emp.first_name} {emp.last_name} ({emp.job_title}) zarabia ${emp.salary}')
    # print(f'Pracownik {emp[1]} {emp[2]} ({emp[3]}) zarabia {emp[4]} USD')
    # modyfikacja zabroniona: emp.first_name = 'Jan'

# Dla obiektów namedtuple możliwy jest dostęp dol pól poprzez nazwę atrybutu oraz przez numer pozycji
