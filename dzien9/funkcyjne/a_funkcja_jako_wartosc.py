def powitaj():
    print('Witaj serdecznie!')

def pozegnaj():
    print('Do widzenia.')


print('Początek programu')

# Zauważmy, że nazwy `powitaj` i `pozegnaj` mają status zmiennych globalnych. Czy to oznacza, że funkcje są zmiennymi?
# W Pythonie tak!
print('globals:', globals())
print('zmienna `powitaj`:', powitaj)
powitaj()

print('\n---- badanie zmiennej f--')
# Funkcję można wpisać do zmiennej
f = powitaj
print('f:', f)
# Teraz w zmiennej f mamy funkcję i możemy ją wywołać
f()
f = pozegnaj
print('f:', f)
f()
print('--------\n')

# Funkcja może być elementem kolekcji (lista, słownik...)

funkcje = [powitaj, lambda: print('Mówię coś'), pozegnaj]
print(funkcje)
for funkcja in funkcje:
    funkcja()
# ↑ Skojarzenie: w szugladzie leżą trzy zabawki.
# Po kolei biorę każdą z nich i naciskamguzik, aby zadziałała...
print("=" * 20)

# Teraz funkcje, które biorą dwa argumenty i zwracają wynik, jak działania matematyczne.
def dodaj(a, b):
    return a+b

def pomnoz(x, y):
    return x*y

def liczba_z_cyfr(a, b):
    return 10*a + b


arg1 = 5
arg2 = 3
for funkcja in dodaj, pomnoz, liczba_z_cyfr:
    wynik = funkcja(arg1, arg2)
    print(f'Funkcja {funkcja.__name__} dla argumentów {arg1} i {arg2} dała wynik {wynik}')

