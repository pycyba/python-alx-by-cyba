from random import randint

x = randint(1, 20)
y = randint(1, 20)
poprawny_wynik = x * y
ile_prob = 0

while True:
    odp = int(input(f'Ile to jest {x}×{y}? '))
    ile_prob += 1
    if odp == poprawny_wynik:
        break
    print('Błędna odpowiedź')

print(f'Poprawny wynik!. Udało się w {ile_prob} próbie')
