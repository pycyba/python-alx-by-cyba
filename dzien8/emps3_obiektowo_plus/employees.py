from datetime import date
from decimal import Decimal

class Employee:
    nazwy_kolumn = ('employee_id', 'first_name', 'last_name', 'job_title', 'salary', 'hire_date',
                 'department_name', 'address', 'postal_code', 'city', 'country')

    SEP = ';'

    def __init__(self, employee_id, first_name, last_name, job_title, salary, hire_date, department_name, address, postal_code, city, country):
        self.employee_id = int(employee_id)
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.job_title = str(job_title)
        self.salary = Decimal(salary)
        self.hire_date = date.fromisoformat(hire_date)
        self.department_name = str(department_name)
        self.address = str(address)
        self.postal_code = str(postal_code)
        self.city = str(city)
        self.country = str(country)


    def __str__(self):
        return f'Pracownik nr {self.employee_id}: {self.first_name} {self.last_name} ({self.job_title}), pensja {self.salary}'

    def staz_pracy(self):
        # return (date.today().year - self.hire_date.year)
        return int((date.today() - self.hire_date).days / 365.2425)


    # Tutaj wczytywanie danych z pliku zrobimy jako metodę statyczną wewnątrz klasy.
    # Metoda statyczna nie przyjmuje parametru self i jest wywoływana nie na obiekcie, tylko na klasie.
    @staticmethod
    def read_csv(file_path='emps.csv'):
        with open(file_path, mode='r', encoding='utf-8') as file:
            next(file)
            return [Employee(*(line.strip().split(Employee.SEP))) for line in file]


    # tylko aby wyjaśnić kroki operajci:
    @staticmethod
    def read_csv_rozwlekle(file_path='emps.csv'):
        with open(file_path, mode='r', encoding='utf-8') as file:
            file.readline()
            lista = []
            for line in file:
                t = line.strip().split(Employee.SEP)
                # emp = Employee(t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9], t[10])
                emp = Employee(*t)
                lista.append(emp)
            return lista


    # W tej wersji funkcja działa na zasadzie generatora - zwraca rekordy dopiero wtedy, gdy są potrzebne aplikacji.
    # Może się to przydać, gdybyśmy chcieli czytać BARDZO DUŻE dane - wtedy nie wczytają się na raz do pamięci, tylko będą pobierane po jednym rekordzie
    # Ograniczeniem z kolei jest to, że dane można przejrzeć tylko raz - nie ma listy, którą można przeglądać wielokrotnie.
    @staticmethod
    def read_csv_generator(file_path='emps.csv'):
        with open(file_path, mode='r', encoding='utf-8') as file:
            file.readline()
            for line in file:
                yield Employee(*(line.strip().split(Employee.SEP)))


    @staticmethod
    def write_csv(emps, sciezka):
        with open(sciezka, mode='w', encoding='utf-8') as file:
            print(*Employee.nazwy_kolumn, sep=Employee.SEP, file=file)
            for emp in emps:
                print(*emp.__dict__.values(), sep=Employee.SEP, file=file)
