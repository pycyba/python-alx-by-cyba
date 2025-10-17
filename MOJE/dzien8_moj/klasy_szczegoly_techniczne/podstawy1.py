# Przykład klasy z pustą definicją
class Osoba:
    pass


# Możemy tworzyć obiekty tej klasy
a = Osoba()
b = Osoba()
print(a)
print(b)

# Szok dla programistów C++ / Java / C#
# W Pythonie do obiektu w dowolnym momencie można dodać nowy atrybut,
# nawet jeśli w klasie nie było o nim mowy
a.imie = 'Ala'
a.nazwisko = 'Kowalska'
b.imie = 'Bartek'

print(a.imie, a.nazwisko)
print(b.imie)
# problem - jeśli różne obiekty będą miały różne zestawy atrybutów, to łatwo popełmić błędy
# i na pewno nie o to chodzi w OOP
#print(b.nazwisko)

# Standardowe klasy Pythona, jak list, są zabezpieczone przed dodawnaiem nieoczekiwanych atrybutów
lista = []
# lista.ogonek = 'ą'
# print(lista.ogonek)
