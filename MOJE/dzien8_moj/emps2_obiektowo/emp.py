from typing import List

class Employee:
    def __init__(self, employee_id, first_name, last_name, job_title, salary, hire_date,
                 department_name, address, postal_code, city, country):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.salary = salary
        self.hire_date = hire_date
        self.department_name = department_name
        self.address = address
        self.postal_code = postal_code
        self.city = city
        self.country = country

    def __str__(self):
        return f'Employee {self.employee_id}: {self.first_name} {self.last_name} ({self.job_title}), salary: {self.salary}, department: {self.department_name}'


# w tej wersji funkcje odczytu / zapisu pliku są zdefiniowane poza klasą
# są to "zwykłe funkcje" umieszczone w tym samym pliku, co klasa
def wczytaj(sciezka:str) -> List[Employee]:
    lista = []
    with open(sciezka, mode='r', encoding='UTF-8') as wejscie:
        wejscie.readline()
        for linia in wejscie:
            t = linia.strip().split(';')
            emp = Employee(int(t[0]), t[1], t[2], t[3], int(t[4]), t[5], t[6], t[7], t[8], t[9], t[10])
            lista.append(emp)
    return lista

