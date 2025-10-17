class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def zapamietaj_numer_buta(self, nr):
        self.numer_buta = nr


a = Osoba('Ala', 'Kowalska')
b = Osoba('Bartek', 'Malinowski')

print(a.imie, a.nazwisko)
print(b.imie, b.nazwisko)
print()

# Do istniejącego obiektu można dodać atrybut, którego tam wcześniej nie było
# Ale uwaga! To jest raczej zła praktyka, nie polecamy w normalnym programowaniu
a.zwierze = 'kot'
print(a.imie, 'ma', a.zwierze)
# print(b.imie, 'ma', b.zwierze) # AttributeError:

b.zapamietaj_numer_buta(44)
print(b.numer_buta)
print()

# Tak naprawdę za każdym obiektem kryje się pewien słownik - w którym zpaisane są wszystkie atrybuty tego obiektu
slownik_a = a.__dict__
slownik_b = b.__dict__
print(slownik_a)
print(slownik_b)

# Gdy zmienię atrubyty w sposób obiektowy
a.imie = 'Alicja'
a.zwierze = 'tygrys'
# to zmiany są widoczne poprzez słownik
print(slownik_a)

slownik_a["nazwisko"] = 'Malinowska'
print(slownik_a)
print(a.imie, a.nazwisko, 'ma', a.zwierze)

del a.zwierze
print(slownik_a)
# print(a.zwierze)
