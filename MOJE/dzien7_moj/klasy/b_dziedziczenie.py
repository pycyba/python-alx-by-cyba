








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
        print(f'Nazywam się {self.imie} {self.nazwisko} i mam {self.wiek} lat.')


class Student(Osoba):
    def __init__(self, imie, nazwisko, wiek, kierunek, rok):
        super().__init__(imie, nazwisko, wiek)
        self.kierunek = kierunek
        self.rok = rok
        self.oceny = []

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    def srednia_ocen(self):
        from statistics import mean
        return mean(self.oceny) if self.oceny else 0

    # W podklasie można przedefiniować ('override') metodę, która
    # istnieje już w nadklasie. Wtedy metoda o tej samej nazwie
    # będzie inaczej działać dla obiektów nadklasy, a inaczej obiektów podklasy.
    def przedstaw_sie(self):
        print(f'Hej, jestem {self.imie} {self.nazwisko}, studiuję na {self.rok} roku kierunku {self.kierunek}.')


osoba = Osoba('Ala', 'Kowalska', 40)
print(type(osoba))
print(osoba)
print(osoba.wiek)
osoba.przedstaw_sie()
#ERR print(osoba.kierunek)
#ERR print(osoba.srednia_ocen())
print()

student = Student('Jan', 'Kowalski', 20, 'medycyna', 2)
print(type(student))
print(student)
print(student.wiek)
print(student.kierunek)
student.przedstaw_sie()
student.dodaj_ocene(5)
student.dodaj_ocene(3)
student.dodaj_ocene(3)
print(student.srednia_ocen())
print()

lista_osob = [osoba,
              student,
              Osoba('Ola', 'Malinowska', 30),
              Osoba('Ula', 'Nowakowska', 10),
              Student('Adam', 'Abacki', 25, 'geologia', 5)]

for ktos in lista_osob:
    ktos.przedstaw_sie()
print()


for ktos in lista_osob:
    print('Obiekt klasy', type(ktos).__name__, 'o zawartości', ktos)
    # (Student jest Osobą w tym sensie:)
    if isinstance(ktos, Osoba):
        print('To jest instancja klasy Osoba i ma imie', ktos.imie)
    if isinstance(ktos, Student):
        print('To jest instancja klasy Student, kierunek =', ktos.kierunek)
    print()

