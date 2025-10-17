
def pierwsza():
    print('Początek funkcji pierwsza')
    print('aaa, kotki dwa')
    print('Koniec funkcji pierwsza')


print('Funkcja pierwsza została zdefiniowana')
print('Sama funkcja to jest', pierwsza)

print('Teraz ją uruchomię:')
pierwsza()
print('\nTeraz ją znowu uruchomię:')
pierwsza()
print()

# Normalnie wszystkie funkcje definiuje się na początku pliku
# lub w oddzielnych plikach (i wtedy się je importuje)
# Ale tutaj zobaczmy, że da się funkcję zdefiniować w środku programu - jest dostępna od tego miejsca w dół

# Ta funkcja przyjmuje parametr.
def witaj(imie):
    print(f'Witaj {imie}!')

# w miejscu wywołania w nawiasach wpisuje się wartość parametru
witaj('Ala')
witaj('Tomek')
kto = 'Ania'
witaj(kto)
witaj(imie='Patryk')
#ERR witaj()
print()

# Funkcja może zwracać wynik - służy do tego return
def pole_prostokata(a, b):
    return a * b

# Samo wywołanie takiej funkcji nie spowoduje pojawienia się wyniku
pole_prostokata(2, 3)

# wynik funkcji można np. zapisać do zmiennej
pole = pole_prostokata(3, 5)

print('Funkcja pole_prostokata została wywołana i dla argumentów 3,5 dała wynik', pole)
print(pole_prostokata(3, 4))

print('\nKoniec programu')
