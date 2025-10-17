class Osoba:

    def zainicjuj(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        print(f'Nazywam się {self.imie} {self.nazwisko}')


a = Osoba()
a.zainicjuj('Ala', 'Kowalska')
a.przedstaw_sie()

b = Osoba()
b.imie = 'Bartek'
b.nazwisko = 'Malinowski'
# aby uruchomić metodę przedstaw_sie, aby ona zadziałała, atrybuty imie i nazwisko muszą być ustawione
b.przedstaw_sie()
