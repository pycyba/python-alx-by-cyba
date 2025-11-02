from random import randint

x = randint(1, 20)
y = randint(1, 20)

odp = int(input(f'Ile to jest {x}×{y}? '))

# W tej wersji nie będzie jeszcze pętli, tylko if
if odp == x*y:
    print('Poprawny wynik!')
else:
    print('Błędny wynik')
