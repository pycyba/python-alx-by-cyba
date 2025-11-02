from random import randrange

ZAKRES = 1000

liczba = randrange(ZAKRES)
ile_prob = 0

while True:
    ile_prob += 1
    propozycja = int(input(f'Podaj szukaną liczbę: '))
    if propozycja < liczba:
        print('Za mało. Szukana liczba jest większa.')
    elif propozycja > liczba:
        print('Za dużo. Szukana liczba jest mniejsza.')
    else:
        print(f'Brawo! Udało Ci się odgadnąć w {ile_prob} próbie.')
        break
