# standardowe wyjście, to kanał, poprzez który program domyślnie wypisuje teksty za pomocą print

print('Hello world')

# więcej o możliwościach print w prykładzie h_wyjscie.py

# standardowe wejście, to domyślny kanał, przez który program może wczytać dane
# domyślnie: konsola, a w zasadzie klawiatura użytkownika

# aby program Pythona takie dane wejściowe wczytał, używa się funkcji input

# Program zatrzyma się i poczeka aż użytkownik wpisze linię tekstu i naciśnie enter
tekst = input()

print('Napisałeś:', tekst)
print()

# Zazwyczaj w input wpisuje się "tekst zachęty", czyli polecenie/pytanie do użytkownika

imie = input('Podaj swoje imię: ')
print('Witaj', imie)
print()

# Aby po pytaniu program przeszedł do nowej linii, użyj \n
tekst = input('Podaj tekst:\n')
print('Napisałeś:', tekst)
print()

# Jak wczytać liczbę?

# x = input('Podaj pierwszą liczbę: ')
# y = input('Podaj drugą liczbę: ')
# suma = x + y
# print(suma)  # dodawało tekstowo

x = int(input('Podaj pierwszą liczbę: '))
y = int(input('Podaj drugą liczbę: '))

suma = x + y
print(suma)
