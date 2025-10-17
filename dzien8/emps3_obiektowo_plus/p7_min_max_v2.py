from employees import Employee

max = None
min = None

# obiekty prztwarze są pojedynczo dzieki temu, że to jest generator (czyli że jest tam `yield` a nie `return`)
# można połączyć obiektowość z oszczędzaniem pamięci
# nawet, gdyby w pliku było więcej danych, niż mieści się w pamięci, to ten program by dał radę
for emp in Employee.read_csv_generator():
    if max is None or emp.salary > max.salary:
        max = emp
    if min is None or emp.salary < min.salary:
        min = emp

print('Najbogatszy:', max)
print('Najbiedniejszy:', min)

