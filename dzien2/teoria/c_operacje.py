# Operacje matematyczne, dostępne dla liczb
print(' 5 + 3 = ', 5 + 3)  # dodawanie
print(' 5 - 3 = ', 5 - 3)  # odejmowanie
print(' 5 * 3 = ', 5 * 3)  # mnożenie
print(' 5 / 3 = ', 5 / 3)  # dzielenie, które w wyniku daje float-a
print(' 5 //3 = ', 5 // 3)  # dzielenie, które w wyniku zwraca część całkowitą jako int
print(' 5 % 3 = ', 5 % 3) # reszta z dzielenia
print('-5 % 3 = ', -5 % 3) # reszta z dzielenia
print(' 5 % -3 =', 5 % -3) # reszta z dzielenia z ujemnym dzielnikiem - wynik ujemny
print(' 5 **3 = ', 5 ** 3) # potęgowanie
print(' 2 ** 0.5 = ', 2 ** 0.5) # pierwiastek
print(' -2 ** 0.5 = ', (-2) ** 0.5) # pierwiastek z ujemnej - wynikiem liczba zespolona
print()
y = 2+3j
print(y, 'typu', type(y))
jednostka_urojona = 1j
print(jednostka_urojona, jednostka_urojona**2)
print()

print('Przykłady dzielenia:')
for x in range(-10, 11):
    print(f'{x:3} / 3 = {x / 3:6.3f}    {x:3} // 3 = {x // 3:3}    {x:3} % 3 = {x % 3:3}')

print()

# Niektóre operatory są dostępne dla różnych typów, np. liczb, napisów, kolekcji,
# ale działają w inny sposób.

liczba1 = 12
liczba2 = 34

napis1 = "12"
napis2 = "34"

print('Typ liczby', type(liczba1), type(liczba1 + liczba2))
print('Typ napisu', type(napis1), type(napis1 + napis2))
print()

print('Dodawanie liczb', liczba1 + liczba2)
print('Dodawanie napisów', napis1 + napis2)
print()

print('Mnożenie liczb', liczba1 * 5)
print('Mnożenie napisu przez liczbę', napis1 * 5)
#EXN print('Mnożenie napisów przez siebie', napis1 * napis2)
print()

lista = ['Gdańsk', 'Sopot', 'Gdynia']
print(lista)
print(lista * 4)


# Jeśli chcemy zmodyfikować zmienną, np. zwiększyć o podaną "deltę"
x = 100
y = 200

# To można po pierwsze tak:
x = x + 5
print(x)

# A po drugie tak:
y += 6
print(y)

# Istnieją też -=   *=   /= ....
# W Pythonie nie istnieje operator ++
