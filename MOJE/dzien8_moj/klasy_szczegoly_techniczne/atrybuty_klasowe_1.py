# My uczyliśmy się tworzenia atrybutów w metodzie init
# Ale w Pythonie można też definiować atrybuty na poziomie klasy, jka np. w C++ czy Javie.

# Ale to działa dziwnie...

class Osoba:
    imie = 'IMIĘ'
    nazwisko = 'NAZWISKO'
    # w realu byłoby raczej
    # imie = ''
    # nawisko = ''

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'

    def hello(self):
        return f'Hello {self.imie}'


class Student(Osoba):
    # ta lista będzie współdzielona przez wszystkie obiekty
    # analogia: zmienne statyczne w Javie czy C#
    oceny = []

    def dodaj_ocene(self, ocena):
        # dwie pierwsze wersje dają efekt "wspólnej listy dla wszystkich studentów"
        self.oceny.append(ocena)
        # self.oceny += [ocena]
        # trzecia wersja działa poprawnie, ale to mało wydajne...
        # self.oceny = self.oceny + [ocena]

    def srednia(self):
        return sum(self.oceny) / len(self.oceny)

    def __str__(self):
        return super().__str__() + f' z ocenami {self.oceny}'


o = Osoba()
print(o.imie)
print(o)
print('etap1, atrybuty obiektu:', o.__dict__)
print('atrybuty klasy:', Osoba.__dict__)
o.imie = 'Jan'
o.nazwisko = 'Kowalski'
print(o.imie)
print(o)
print('etap2, atrybuty obiektu:', o.__dict__)
print('atrybuty klasy:', Osoba.__dict__)
print()

o2 = Osoba()
print(o2)
o2.imie = 'Ala'
o2.nazwisko = 'Kowalska'
print(o2)
print(o)
print()
# W klasie Osoba takie działanie jest jak najbardziej OK
# Dlatego że atrybuty imie i nazwisko zawierają wartości typu str
# a typ str jest NIEMUTOWALNY. Podobnie byloby z int, float itp.

a = Student()
print(a)
a.imie = 'Adam'
a.nazwisko = 'Abacki'
print(a)
print()

b = Student()
print(b)
b.imie = 'Bartek'
b.nazwisko = 'Babecki'
print(b)

print()
print(a)
print(b)
# Do tej pory to działało dobrze

a.dodaj_ocene(5)
a.dodaj_ocene(5)
a.oceny.append(5)
print(a, a.srednia())

print()
b.dodaj_ocene(3)

print(a, a.srednia())

print('Oceny Adama:', a.oceny)
print('Oceny Bartka:', b.oceny)
print(a.oceny is b.oceny)
print('Oceny z klasy:', Student.oceny)

# Morał: to jest TA SAMA lista
# Atrybut oceny jest tworzony w klasie!!!
# Różne obiekty mają do niego dostęp, ale to jest ten sam obiekt

# Ze stringami nie ma problemu, bo stringi sa "niemutowalne" i w obiektach możemy wpisac inne stringi - ale to będą nowe obiekty
# Ale lista jest "mutowalna" i obiekty mogą modyfikować wspólny obiekt - wspólną listą.
