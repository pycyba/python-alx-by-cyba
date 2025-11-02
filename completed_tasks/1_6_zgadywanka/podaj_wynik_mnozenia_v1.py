from random import randint

x = randint(1, 20)
y = randint(1, 20)
poprawny_wynik = x * y
ile_prob = 1

odp = int(input(f'Ile to jest {x}×{y}? '))

while odp != poprawny_wynik:
    odp = int(input('Błędny wynik, spróbuj jeszcze raz: '))
    ile_prob += 1

print(f'Poprawny wynik!. Udało się w {ile_prob} próbie')
