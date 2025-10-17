# Prosta klasa zapisana w najbardziej typowy sposób:

class Osoba:
    def __init__(self, imie, nazwisko, pesel=None):
        print('a kuku')
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel

    def __str__(self):
        pesel_info = f', PESEL: {self.pesel}' if self.pesel else ''
        return f'{self.imie} {self.nazwisko}{pesel_info}'

    def przedstaw_sie(self):
        print(f'Nazywam się {self.imie} {self.nazwisko}.')



# Na funkcje, które są definiowane wewnątrz klas mówimy 'metoda' (method)

# "normalny program" :
# Teraz utworzymy obiekt klasy Osoba i wpiszemy go(*) do zmiennej a
a = Osoba(imie='Ala', nazwisko='Kowalska')
print('a:', a)
# na obiekcie można wywołać metodę:
a.przedstaw_sie()
# Jeśli obiekt posiada atrybuty (zmienne w obiekcie), można z nich korzystać w taki sposób:
print('Imię pierwszej osoby:', a.imie)
a.imie = 'Alicja'
a.przedstaw_sie()


b = Osoba('Bartek', 'Malinowski', '85050512345')
c = Osoba('Celina', 'Ciechowska')
print('b:', b)
print('c:', c)
wynik_str = str(c)
print(wynik_str)

b.przedstaw_sie()
c.przedstaw_sie()

# (*) – tak naprawdę do zmiennych w Pythonie nie są wpisywane całe obiekty, tylko ich adresy
# na co można mówić "referencja do obiektu" lub "wskaźnik do obiektu"
