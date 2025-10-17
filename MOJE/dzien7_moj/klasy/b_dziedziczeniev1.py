class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def __str__(self):
        return f'{self.imie} {self.nazwisko} ({self.wiek} lat)'

    def pelnoletnia(self):
        return self.wiek >= 18

    def przedstaw_sie(self):
        print(f'Nazywam się {self.imie} {self.nazwisko}')


class Student(Osoba):
    pass


osoba = Osoba('Ala', 'Kowalska', 40)
print(type(osoba))
print(osoba)
print(osoba.wiek)
osoba.przedstaw_sie()
print()

student = Student('Jan', 'Kowalski', 20)
print(type(student))
print(student)
print(student.wiek)
student.przedstaw_sie()

