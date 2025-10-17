class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        print(f'Nazywam się {self.imie} {self.nazwisko}')


# Python automatycznie uruchamia metodę init, gdy tworzymy obiekt
a = Osoba('Ala', 'Kowalska')
a.przedstaw_sie()

b = Osoba('Bartek', 'Malinowski')
b.przedstaw_sie()

# Tak wygląda proces tworzenia obiektu zapisany bardziej niskopoziomowo:
# 1) utworzenie pustego niezainicjowanego obiektu za pomocą metody klasowej __new__
# 2) wykonanie na tym obiekcie metody __init__ z przekazanmi parametrami
c = object.__new__(Osoba)
c.__init__('Celina', 'Cicha')
print(type(c))
c.przedstaw_sie()

# Metody takie jak init i przedstaw_sie można też wywoływać z poziomu klasy
# - wówczas parametr self też przekazujemy w sposób jawny
d = Osoba.__new__(Osoba)
Osoba.__init__(d, 'Darek', 'Kowalski')
Osoba.przedstaw_sie(d)
