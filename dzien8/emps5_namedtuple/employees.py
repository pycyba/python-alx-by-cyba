from collections import namedtuple

nazwy_kolumn = ('employee_id', 'first_name', 'last_name', 'job_title', 'salary', 'hire_date',
                 'department_name', 'address', 'postal_code', 'city', 'country')

Employee = namedtuple('Employee', nazwy_kolumn)


def read_csv(path):
    emps = []
    with open(path, mode='r', encoding='utf-8') as file:
        file.readline()
        for line in file:
            t = line.strip().split(';')
            emp = Employee(int(t[0]), t[1], t[2], t[3], int(t[4]), *t[5:])
            emps.append(emp)
    return emps
