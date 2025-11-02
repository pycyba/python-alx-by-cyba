from random import randrange

ZAKRES = 1000

liczba = randrange(ZAKRES)
ile_prob = 1

propozycja = int(input(f'Podaj szukaną liczbę: '))

while propozycja != liczba:
    ile_prob += 1
    if propozycja < liczba:
        print('Za mało. Podaj większą liczbę: ', end='')
    if propozycja > liczba:
        print('Za dużo. Podaj mniejszą liczbę: ', end='')
    propozycja = int(input())

print(f'Brawo! Udało Ci się odgadnąć w {ile_prob} próbie.')
