# @dataclass automatycznie generuje metody init, repr, str i eq
# które działają we właściwy sposób dla rekordów z polami takimi, jak wymienione w klasie
# od Pythona 3.7

from dataclasses import dataclass

@dataclass
class Employee:
    employee_id:int
    first_name:str
    last_name:str
    job_title:str
    salary:int
    hire_date:str
    department_name:str
    address:str
    postal_code:str
    city:str
    country:str

    nazwy_kolumn = ('employee_id', 'first_name', 'last_name', 'job_title', 'salary', 'hire_date',
                    'department_name', 'address', 'postal_code', 'city', 'country')

    SEP = ';'

    @property
    def wszystkie_pola(self):
        # pobranie wartości wszystkich atrybutów obiektu w takiej kolejności, jak wpisane w init
        return self.__dict__.values()
        # gdybyśmy mieli wątpliwości co do olejności kolumn, to można też tak:
        # return [self.__dict__[kolumna] for kolumna in Employee.nazwy_kolumn]

    # Inaczej, niż w przypadku namedtuple, w klasie tworzonej za pomocą @dataclass można zdefiniować własne metody
    def zmien_pensje(self, zmiana):
        self.salary += zmiana

    @staticmethod
    def read_csv(sciezka):
        lista = []
        with open(sciezka, mode='r', encoding='utf-8') as plik:
            plik.readline()
            for linia in plik:
                t = linia.strip().split(Employee.SEP)
                emp = Employee(int(t[0]), t[1], t[2], t[3], int(t[4]), *t[5:])
                lista.append(emp)
        return lista

    @staticmethod
    def write_csv(emps, sciezka):
        with open(sciezka, mode='w', encoding='utf-8') as plik:
            print(*Employee.nazwy_kolumn, sep=Employee.SEP, file=plik)
            for emp in emps:
                print(*emp.wszystkie_pola, sep=Employee.SEP, file=plik)
