# Wersja poprawiona - wewnątrz init tworzona jest zawsze nowa lista, być może wypełniona początkowymi elementami.
class Student:
    def __init__(self, imie, nazwisko, oceny=()):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = list(oceny)

    def init_inna_wersja(self, imie, nazwisko, oceny=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = list(oceny) if oceny else []

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    def srednia_ocen(self):
        return sum(self.oceny) / len(self.oceny)


adam = Student('Adam', 'Abacki', [3,4,5])
print('adam:', adam.srednia_ocen())

basia = Student('Barbara', 'Rabarbar')
basia.dodaj_ocene(5)
basia.dodaj_ocene(5)
print('basia:', basia.srednia_ocen())

cezary = Student('Cezary', 'Inny')
cezary.dodaj_ocene(2)
cezary.dodaj_ocene(3)
cezary.dodaj_ocene(2)
print('cezary:', cezary.srednia_ocen())
print('basia:', basia.srednia_ocen())
print()
print('oceny adama:', adam.oceny)
print('oceny basi:', basia.oceny)
print('oceny cezarego:', cezary.oceny)

l = [3,3,3]
dorota = Student('Dorota', 'X', l)
print('dorota:', dorota.srednia_ocen())

l.append(5)
print('dorota:', dorota.srednia_ocen())

dorota.dodaj_ocene(4)
print('dorota:', dorota.srednia_ocen())
print('l:', l)
